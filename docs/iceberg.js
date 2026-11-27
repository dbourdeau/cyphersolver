// The cipher iceberg (iceberg.html). A wide shot of a berg at sunset, then a red line runs down the iceberg whose
// tiers hold the entries of the page. Everything is drawn here: no models, no images, no audio files.
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.min.js';

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const body = document.body;
const REDUCE = matchMedia('(prefers-reduced-motion: reduce)').matches;
const clamp = (x, a, b) => Math.min(b, Math.max(a, x));
const lerp = (a, b, t) => a + (b - a) * t;
const smooth = (a, b, x) => { const t = clamp((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };
const raw = hex => new THREE.Color().setHex(hex, THREE.LinearSRGBColorSpace);   // a colour used as written, for shaders that skip colour management

/* ------------------------------------------------------------------ the page's own data */
const sections = $$('.ib-ch');
const tiers = $$('.ib-tier').map(sec => ({
  sec, n: +sec.dataset.tier, name: sec.dataset.name, y0: +sec.dataset.y0, y1: +sec.dataset.y1,
  k: sections.indexOf(sec), lis: $$('.ib-items > li', sec)
}));
const items = [];
tiers.forEach(t => t.lis.forEach((li, i) => items.push({
  li, id: li.id, t, i, m: t.lis.length,
  title: $('summary b', li).innerHTML, yr: ($('summary .yr', li) || {}).textContent || '',
  body: $('.ib-body', li)
})));
const openN = (() => { const e = $('[data-ib="open"]'); return e ? parseInt(e.textContent.replace(/\D/g, ''), 10) || 1000 : 1000; })();

try { localStorage.removeItem('ib-list'); } catch (e) {}   // the list switch was removed on 27 Nov 2026; forget a stored choice
main: {

/* ------------------------------------------------------------------ renderer */
const canvas = $('#ib-canvas');
let renderer;
try {
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
} catch (e) { break main; }                // no WebGL: the page stays a list
const SMALL = Math.min(innerWidth, innerHeight) < 700;
renderer.setPixelRatio(Math.min(devicePixelRatio || 1, SMALL ? 1.5 : 1.75));
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
body.classList.add('ib-3d');
$('#ib-hud').hidden = false;

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 5000);
const U = {                       // shared uniforms
  uTime: { value: 0 }, uFogCol: { value: raw(0x0b4a66) }, uFogDen: { value: 0.02 },
  uHaze: { value: raw(0x8a6a7e) }, uShallow: { value: raw(0x2a8fa8) }, uRim: { value: 0 },
  uSun: { value: new THREE.Vector3(0.92, 0.11, -0.3).normalize() }, uUnder: { value: 0 }
};

/* ------------------------------------------------------------------ noise (for the ice) */
const P = new Uint8Array(512); { const p = [...Array(256).keys()]; let s = 7;
  for (let i = 255; i > 0; i--) { s = (s * 16807) % 2147483647; const j = s % (i + 1); [p[i], p[j]] = [p[j], p[i]]; }
  for (let i = 0; i < 512; i++) P[i] = p[i & 255]; }
const G3 = [[1,1,0],[-1,1,0],[1,-1,0],[-1,-1,0],[1,0,1],[-1,0,1],[1,0,-1],[-1,0,-1],[0,1,1],[0,-1,1],[0,1,-1],[0,-1,-1]];
function noise3(x, y, z) {          // classic simplex noise, -1..1
  const F3 = 1 / 3, G = 1 / 6; const s = (x + y + z) * F3;
  const i = Math.floor(x + s), j = Math.floor(y + s), k = Math.floor(z + s); const t = (i + j + k) * G;
  const x0 = x - i + t, y0 = y - j + t, z0 = z - k + t; let i1, j1, k1, i2, j2, k2;
  if (x0 >= y0) { if (y0 >= z0) { i1=1;j1=0;k1=0;i2=1;j2=1;k2=0; } else if (x0 >= z0) { i1=1;j1=0;k1=0;i2=1;j2=0;k2=1; } else { i1=0;j1=0;k1=1;i2=1;j2=0;k2=1; } }
  else { if (y0 < z0) { i1=0;j1=0;k1=1;i2=0;j2=1;k2=1; } else if (x0 < z0) { i1=0;j1=1;k1=0;i2=0;j2=1;k2=1; } else { i1=0;j1=1;k1=0;i2=1;j2=1;k2=0; } }
  const c = [[x0, y0, z0, 0, 0, 0], [x0 - i1 + G, y0 - j1 + G, z0 - k1 + G, i1, j1, k1], [x0 - i2 + 2 * G, y0 - j2 + 2 * G, z0 - k2 + 2 * G, i2, j2, k2], [x0 - 1 + 3 * G, y0 - 1 + 3 * G, z0 - 1 + 3 * G, 1, 1, 1]];
  let n = 0; const ii = i & 255, jj = j & 255, kk = k & 255;
  for (const [a, b, d, di, dj, dk] of c) { let tt = 0.6 - a * a - b * b - d * d; if (tt < 0) continue;
    const g = G3[P[ii + di + P[jj + dj + P[kk + dk]]] % 12]; tt *= tt; n += tt * tt * (g[0] * a + g[1] * b + g[2] * d); }
  return 32 * n;
}
const fbm = (x, y, z, o = 4) => { let a = 0.5, f = 1, s = 0; for (let i = 0; i < o; i++) { s += a * noise3(x * f, y * f, z * f); f *= 2.03; a *= 0.5; } return s; };

/* ------------------------------------------------------------------ the shape of the berg */
const WL_R = 11, HMAX = 14;               // waterline radius, height of the highest peak
const PROFILE = [[0, WL_R], [-1.5, 12.5], [-5, 18], [-12, 27], [-22, 33], [-36, 35], [-52, 33],
  [-66, 29], [-80, 24], [-94, 18], [-105, 11.5], [-112, 6.5], [-116.5, 2.5], [-118, 0.01]];
function baseR(y) {
  if (y >= 0) return WL_R;
  for (let i = 1; i < PROFILE.length; i++) if (y >= PROFILE[i][0]) {
    const [ya, ra] = PROFILE[i - 1], [yb, rb] = PROFILE[i]; const t = (ya - y) / (ya - yb); return lerp(ra, rb, t * t * (3 - 2 * t) * 0.35 + t * 0.65);
  }
  return 0.01;
}
const angD = (a, b) => Math.atan2(Math.sin(a - b), Math.cos(a - b));
function hm(a) {                        // relative height of the ice above water at angle a: one main peak, three lesser ones
  const pk = (c, w, h) => h * Math.exp(-((angD(a, c) / w) ** 2));
  return 0.3 + Math.max(pk(0.74, 0.75, 0.7), pk(1.7, 0.38, 0.42), pk(3.0, 0.8, 0.45), pk(-1.3, 0.6, 0.52), pk(0.2, 0.3, 0.5))
    + 0.08 * noise3(Math.cos(a) * 2.6, 3.3, Math.sin(a) * 2.6);
}
const colH = a => HMAX * hm(a);
function disp(a, y) {                   // relative bulge of the surface at angle a, height y
  const cx = Math.cos(a) * 1.7, cz = Math.sin(a) * 1.7;
  const big = fbm(cx, y * 0.035, cz, 3), small = fbm(cx * 3.1 + 9, y * 0.11, cz * 3.1, 2);
  const shelf = Math.abs(noise3(cx * 0.8, y * 0.02 + 3, cz * 0.8));
  return 1 + 0.17 * big + 0.06 * small - 0.05 * shelf;
}
function topR(a, s) {                  // radius above water, s = 0 at the waterline, 1 at the top of the column
  return WL_R * disp(a, 0) * (1 - 0.62 * Math.pow(s, 1.6)) * (1 + 0.14 * noise3(Math.cos(a) * 3, s * 4, Math.sin(a) * 3));
}
const surfR = (a, y) => y > 0 ? topR(a, Math.min(1, y / colH(a))) : baseR(y) * disp(a, y);
const surfP = (a, y, off = 0) => { const r = surfR(a, y) + off; return new THREE.Vector3(Math.cos(a) * r, y, Math.sin(a) * r); };

function bergGeometry(NA, NYa, NYb, yBot = -118) {
  const pos = [], idx = [], NY = NYa + NYb;
  for (let j = 0; j <= NY; j++) {
    for (let i = 0; i < NA; i++) {
      const a = i / NA * Math.PI * 2; let y, r;
      if (j <= NYa) { const sv = 1 - j / NYa; y = sv * colH(a); r = topR(a, sv); }
      else { y = lerp(0, yBot, (j - NYa) / NYb); r = baseR(y) * disp(a, y); }
      r += noise3(i * 1.31, j * 0.97, 5.5) * (y > 0 ? 0.55 : 0.35);
      pos.push(Math.cos(a) * r, y + noise3(i * 0.7, j * 0.7, 1.7) * (y > 0 ? 0.45 : 0.25) * (j > 0 && j < NY), Math.sin(a) * r);
    }
  }
  let mh = 0; for (let i = 0; i < NA; i++) mh += pos[i * 3 + 1]; mh /= NA;
  const top = pos.length / 3; pos.push(0, mh * 1.05, 0);
  const bot = top + 1; pos.push(0, yBot - 0.5, 0);
  for (let j = 0; j < NY; j++) for (let i = 0; i < NA; i++) {
    const a = j * NA + i, b = j * NA + (i + 1) % NA, c = (j + 1) * NA + i, d = (j + 1) * NA + (i + 1) % NA;
    idx.push(a, c, b, b, c, d);
  }
  for (let i = 0; i < NA; i++) { idx.push(top, i, (i + 1) % NA); idx.push(bot, NY * NA + (i + 1) % NA, NY * NA + i); }
  // the table: pull the first ring's inner fan flat
  let g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setIndex(idx);
  g = g.toNonIndexed(); g.computeVertexNormals();
  return g;
}

/* ------------------------------------------------------------------ shader patches */
const FOG_GLSL = /* glsl */`
uniform vec3 uFogCol; uniform float uFogDen; uniform vec3 uHaze; uniform vec3 uShallow; uniform float uTime; uniform float uRim;
varying vec3 vWP;
vec3 waterTint(vec3 col, vec3 wp){
  float dist = length(wp - cameraPosition);
  if (cameraPosition.y > 0.0) {
    if (wp.y < 0.0) { float k = 1.0 - exp(-(-wp.y * 1.5 + 4.0) * 0.05); col = mix(col * vec3(0.6, 0.86, 0.95), uShallow, k); }
    col = mix(col, uHaze, (1.0 - exp(-dist * 0.0016)) * 0.75);
  } else {
    col = mix(col, uFogCol, 1.0 - exp(-dist * uFogDen));
  }
  return col;
}
float caus(vec2 p, float t){
  vec2 q = p * 0.32; float c = 0.0;
  for (int i = 0; i < 3; i++) { q += vec2(sin(q.y * 1.7 + t * 0.8), cos(q.x * 1.4 - t * 0.6)) * 0.55; c += abs(sin(q.x + q.y)); }
  return pow(clamp(1.0 - c / 3.0, 0.0, 1.0), 3.0);
}`;
function patch(mat, { ice = false, unlit = false } = {}) {
  mat.onBeforeCompile = sh => {
    Object.assign(sh.uniforms, U);
    sh.vertexShader = 'varying vec3 vWP;\n' + sh.vertexShader.replace('#include <project_vertex>',
      '#include <project_vertex>\n#ifdef USE_INSTANCING\n vWP = (modelMatrix * instanceMatrix * vec4(transformed,1.0)).xyz;\n#else\n vWP = (modelMatrix * vec4(transformed,1.0)).xyz;\n#endif');
    sh.fragmentShader = FOG_GLSL + '\n' + sh.fragmentShader.replace('#include <fog_fragment>', 'gl_FragColor.rgb = waterTint(gl_FragColor.rgb, vWP);');
    if (ice) {
      sh.fragmentShader = sh.fragmentShader
        .replace('#include <color_fragment>', `#include <color_fragment>
          if (vWP.y < 0.0) diffuseColor.rgb *= mix(vec3(1.0), vec3(0.55, 0.8, 1.0), smoothstep(0.0, -20.0, vWP.y)) * exp(vWP.y * 0.012);`)
        .replace('#include <normal_fragment_maps>', `#include <normal_fragment_maps>
          if (vWP.y > -0.6) {
            vec3 wn = normalize((vec4(normal, 0.0) * viewMatrix).xyz);
            float steep = 1.0 - clamp(wn.y, 0.0, 1.0);
            float band = 0.5 + 0.5 * sin(vWP.y * 1.9 + sin(vWP.x * 0.31) * 2.2 + sin(vWP.z * 0.27) * 2.0);
            diffuseColor.rgb = mix(diffuseColor.rgb, vec3(0.33, 0.66, 0.9), steep * (0.35 + 0.35 * band));
            diffuseColor.rgb = mix(diffuseColor.rgb, vec3(1.0), smoothstep(0.72, 0.95, wn.y) * 0.85);
            diffuseColor.rgb *= 1.0 - 0.32 * (1.0 - smoothstep(0.0, 1.4, abs(vWP.y - 0.15)));
          }`)
        .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
          { float fr = pow(1.0 - clamp(dot(normal, normalize(vViewPosition)), 0.0, 1.0), 2.4);
            float under = step(vWP.y, 0.0);
            totalEmissiveRadiance += vec3(0.16, 0.62, 0.86) * fr * uRim * under;
            totalEmissiveRadiance += vec3(0.02, 0.09, 0.13) * uRim * under * smoothstep(-10.0, -60.0, vWP.y);
            float cs = smoothstep(-34.0, -0.6, vWP.y) * under * max(normal.y * 0.3 + 0.7, 0.0);
            totalEmissiveRadiance += vec3(0.55, 0.9, 1.0) * caus(vWP.xz + vec2(vWP.y * 0.4), uTime) * cs * 0.9;
            totalEmissiveRadiance += (vec3(0.05, 0.07, 0.1) + vec3(1.0, 0.72, 0.55) * fr * 0.35) * (1.0 - under); }`);
    }
  };
  mat.fog = false;
  return mat;
}
const forceFog = mat => mat;

/* ------------------------------------------------------------------ sky, water, light */
const SKY_GLSL = /* glsl */`
uniform vec3 uSun; uniform float uTime;
float h21(vec2 p){ return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
float h31(vec3 p){ return fract(sin(dot(p, vec3(127.1, 311.7, 74.7))) * 43758.5453); }
float n2(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return mix(mix(h21(i), h21(i+vec2(1,0)), f.x), mix(h21(i+vec2(0,1)), h21(i+vec2(1,1)), f.x), f.y); }
float fb(vec2 p){ float s = 0.0, a = 0.5; for (int i = 0; i < 5; i++){ s += a * n2(p); p *= 2.02; a *= 0.5; } return s; }
vec3 skyColor(vec3 d, float stars){
  float y = d.y;
  vec3 zen = vec3(0.02, 0.035, 0.11), high = vec3(0.07, 0.11, 0.3), mid = vec3(0.32, 0.26, 0.5), hor = vec3(1.0, 0.5, 0.3);
  vec3 c = mix(hor, mid, smoothstep(0.0, 0.13, y)); c = mix(c, high, smoothstep(0.08, 0.38, y)); c = mix(c, zen, smoothstep(0.32, 0.95, y));
  vec2 dh = normalize(d.xz + 1e-5), sh = normalize(uSun.xz);
  float az = max(dot(dh, sh), 0.0), s = max(dot(d, uSun), 0.0);
  c += vec3(1.0, 0.55, 0.28) * pow(az, 5.0) * exp(-max(y, 0.0) * 9.0) * 0.55;
  c += vec3(1.0, 0.78, 0.5) * pow(s, 12.0) * 0.8 + vec3(1.0, 0.95, 0.85) * smoothstep(0.9988, 0.9995, s) * 4.0;
  c = mix(c, vec3(0.55, 0.3, 0.3), smoothstep(0.0, -0.08, y));
  if (y > 0.0) {
    vec2 p = d.xz / (y + 0.2);
    float cl = smoothstep(0.55, 0.82, fb(p * 1.3 + vec2(uTime * 0.006, 0.0)));
    vec3 cc = mix(vec3(0.16, 0.12, 0.26), vec3(1.0, 0.55, 0.32), pow(az, 3.0) * exp(-y * 5.0));
    c = mix(c, cc, cl * 0.7 * smoothstep(0.0, 0.04, y) * (1.0 - smoothstep(0.12, 0.3, y)));
    float azm = atan(d.z, d.x); vec3 aur = vec3(0.0);
    for (int i = 0; i < 3; i++) {
      float fi = float(i);
      float base = 0.07 + 0.05 * sin(azm * 2.0 + uTime * 0.04 + fi * 2.1) + 0.025 * sin(azm * 5.0 - uTime * 0.06 + fi) + fi * 0.06;
      float hh = y - base;
      float cur = smoothstep(-0.012, 0.012, hh) * exp(-max(hh, 0.0) * (4.5 + fi * 2.0));
      float rays = 0.4 + 0.6 * pow(0.5 + 0.5 * sin(azm * 70.0 + fi * 4.0 + sin(azm * 9.0 + uTime * 0.3) * 3.0), 2.0);
      float patchy = smoothstep(0.3, 0.75, n2(vec2(azm * 2.6 + uTime * 0.02 + fi * 7.0, fi * 3.0)));
      aur += mix(vec3(0.12, 1.0, 0.58), vec3(0.8, 0.3, 1.0), smoothstep(0.02, 0.3, hh)) * cur * rays * patchy * (1.0 - fi * 0.2);
    }
    c += aur * 0.6 * (1.0 - 0.85 * pow(az, 3.0));
    if (stars > 0.5) {
      vec3 q = d * 260.0; vec3 cell = floor(q); float hh = h31(cell);
      if (hh > 0.996) { float st = smoothstep(0.12, 0.0, length(fract(q) - 0.5));
        c += vec3(0.85, 0.92, 1.0) * st * smoothstep(0.12, 0.45, y) * (0.55 + 0.45 * sin(uTime * 2.5 + hh * 120.0)); }
    }
  }
  return c;
}`;
const sky = new THREE.Mesh(new THREE.SphereGeometry(2400, 48, 24), new THREE.ShaderMaterial({
  side: THREE.BackSide, depthWrite: false, uniforms: { ...U },
  vertexShader: `varying vec3 vD; void main(){ vD = normalize((modelMatrix * vec4(position,1.0)).xyz - cameraPosition); gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position,1.0); }`,
  fragmentShader: SKY_GLSL + /* glsl */`
    varying vec3 vD; uniform vec3 uFogCol;
    void main(){
      vec3 d = normalize(vD); vec3 c;
      if (cameraPosition.y < 0.0) {        // under water: light from above, dark below, faint shafts
        float k = smoothstep(-0.75, 0.95, d.y), depth = clamp(-cameraPosition.y / 130.0, 0.0, 1.0);
        c = mix(uFogCol * 0.28, uFogCol * 1.9 + vec3(0.0, 0.07, 0.09) * (1.0 - depth), k);
        float a = atan(d.z, d.x);
        c += vec3(0.4, 0.75, 0.85) * pow(max(d.y, 0.0), 2.5) * (0.5 + 0.5 * sin(a * 38.0 + uTime * 0.25) * sin(a * 17.0 - uTime * 0.17)) * 0.12 * (1.0 - depth);
      } else c = skyColor(d, 1.0);
      gl_FragColor = vec4(c, 1.0);
    }`
}));
sky.renderOrder = -10; scene.add(sky);

const water = new THREE.Mesh(new THREE.PlaneGeometry(6000, 6000, 1, 1), new THREE.ShaderMaterial({
  transparent: true, depthWrite: false, side: THREE.DoubleSide, uniforms: { ...U, uDeepC: { value: raw(0x05202f) } },
  vertexShader: `varying vec3 vWP; void main(){ vWP = (modelMatrix * vec4(position,1.0)).xyz; gl_Position = projectionMatrix * viewMatrix * vec4(vWP,1.0); }`,
  fragmentShader: SKY_GLSL + /* glsl */`
    varying vec3 vWP; uniform vec3 uDeepC, uFogCol, uHaze; uniform float uFogDen;
    vec2 wv(vec2 p, vec2 d, float f, float a, float s){ float ph = dot(p, d) * f + uTime * s; return d * cos(ph) * f * a; }
    void main(){
      vec2 p = vWP.xz; vec2 g = vec2(0.0);
      g += wv(p, normalize(vec2(1.0, 0.3)), 0.09, 0.9, 1.1); g += wv(p, normalize(vec2(-0.4, 1.0)), 0.16, 0.45, 1.5);
      g += wv(p, normalize(vec2(0.7, -0.8)), 0.37, 0.16, 2.3); g += wv(p, normalize(vec2(-1.0, -0.2)), 0.83, 0.06, 3.1);
      g += wv(p, normalize(vec2(0.2, 1.0)), 1.9, 0.02, 4.7);
      vec3 N = normalize(vec3(-g.x, 1.0, -g.y));
      vec3 V = normalize(cameraPosition - vWP); float dist = length(cameraPosition - vWP);
      vec3 col; float al;
      if (cameraPosition.y >= 0.0) {
        float fr = 0.02 + 0.98 * pow(1.0 - max(dot(N, V), 0.0), 5.0);
        vec3 R = reflect(-V, N); R.y = max(abs(R.y), 0.015);
        vec3 sk = skyColor(R, 0.0);
        float sp = pow(max(dot(R, uSun), 0.0), 300.0) * 7.0 + pow(max(dot(R, uSun), 0.0), 18.0) * 0.3;
        col = mix(uDeepC, sk, fr) + vec3(1.0, 0.66, 0.4) * sp;
        float far = 1.0 - exp(-dist * 0.0011);
        col = mix(col, skyColor(normalize(vec3(-V.x, 0.004, -V.z)), 0.0), far * 0.92);
        al = clamp(mix(0.58, 1.0, fr) + far, 0.0, 1.0);
      } else {
        vec3 dir = -V; float up = dir.y;
        float win = smoothstep(0.62, 0.72, up);
        vec3 inside = mix(vec3(0.55, 0.85, 0.92), vec3(0.95, 0.98, 1.0), smoothstep(0.7, 0.98, up + N.x * 0.15));
        col = mix(uFogCol * 1.35 + vec3(0.02, 0.08, 0.1), inside, win);
        col += vec3(0.5, 0.8, 0.9) * (N.x * N.z * 40.0) * win;
        col = mix(col, uFogCol, 1.0 - exp(-dist * uFogDen * 0.8));
        al = 1.0;
      }
      gl_FragColor = vec4(col, al);
    }`
}));
water.rotation.x = -Math.PI / 2; water.renderOrder = 5; scene.add(water);

const sun = new THREE.DirectionalLight(0xffb27a, 3.2); sun.position.copy(U.uSun.value).multiplyScalar(100); scene.add(sun);
const hemi = new THREE.HemisphereLight(0x8fa4ff, 0x1d4a6a, 1.5); scene.add(hemi);

/* ------------------------------------------------------------------ the iceberg */
const iceMat = patch(forceFog(new THREE.MeshPhysicalMaterial({ color: 0xf2f8ff, roughness: 0.3, metalness: 0.0, clearcoat: 0.6,
  clearcoatRoughness: 0.25, flatShading: true })), { ice: true });
{
  const envScene = new THREE.Scene(); envScene.add(new THREE.Mesh(sky.geometry, sky.material));
  const pm = new THREE.PMREMGenerator(renderer); iceMat.envMap = pm.fromScene(envScene, 0.02, 1, 5000).texture; iceMat.envMapIntensity = 0.85; pm.dispose();
}
const berg = new THREE.Mesh(bergGeometry(SMALL ? 72 : 108, SMALL ? 26 : 40, SMALL ? 96 : 140), iceMat);
scene.add(berg);
const foam = (() => {
  const N = 220, pos = [], uv = [], ix = [];
  for (let i = 0; i <= N; i++) { const a = i / N * Math.PI * 2, r0 = surfR(a, 0.02) - 0.25;
    for (const [k, r] of [[0, r0], [1, r0 + 4.5]]) { pos.push(Math.cos(a) * r, 0.04, Math.sin(a) * r); uv.push(i / N, k); }
    if (i) { const b = i * 2; ix.push(b - 2, b - 1, b, b, b - 1, b + 1); } }
  const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2)); g.setIndex(ix);
  const m = new THREE.ShaderMaterial({ transparent: true, depthWrite: false, side: THREE.DoubleSide, uniforms: { ...U },
    vertexShader: `varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`,
    fragmentShader: SKY_GLSL + `varying vec2 vUv; void main(){
      float n = fb(vec2(vUv.x * 90.0, vUv.y * 4.0 - uTime * 0.35)) * 0.6 + fb(vec2(vUv.x * 210.0 + 5.0, vUv.y * 9.0 + uTime * 0.2)) * 0.4;
      float edge = pow(1.0 - vUv.y, 7.0), spread = smoothstep(0.5, 0.72, n) * pow(1.0 - vUv.y, 1.6);
      gl_FragColor = vec4(vec3(0.95, 0.93, 0.98), clamp(edge * 0.8 + spread * 0.75, 0.0, 1.0)); }` });
  const f = new THREE.Mesh(g, m); f.renderOrder = 7; scene.add(f); return f;
})();
// far bergs on the horizon, for scale
const farG = bergGeometry(36, 12, 16, -30);
[[-0.6, 520, 0.28], [0.35, 760, 0.42], [2.4, 640, 0.22], [-2.2, 900, 0.5], [1.2, 1100, 0.35]].forEach(([a, d, s]) => {
  const m = new THREE.Mesh(farG, iceMat); m.scale.set(s, s * 1.1, s); m.position.set(Math.cos(a) * d, -0.6, Math.sin(a) * d); m.rotation.y = a * 3; scene.add(m);
});

/* ------------------------------------------------------------------ the leaf: Penn LJS 51, f. 106v */
// The seven cipher lines Ibn al-Qabaqibi sent to the compiler, from the crop published with the write-up (OPenn, public
// domain). It drifts in the abyss beside its entry, and the red reading runs over it, right to left, as you pass.
const LW = 6.4, LH = LW * 938 / 1100;
const leafTex = new THREE.TextureLoader().load('qaysarani1350_cipher.jpg');
leafTex.colorSpace = THREE.SRGBColorSpace; leafTex.anisotropy = 8;
const leafU = { uSweep: { value: 0 }, uGloss: { value: 0 }, uTime: U.uTime };
const leafMat = new THREE.MeshBasicMaterial({ map: leafTex, transparent: true, toneMapped: false, side: THREE.DoubleSide, depthWrite: false });
const fogOBC = patch(new THREE.MeshBasicMaterial()).onBeforeCompile;
leafMat.onBeforeCompile = sh => {
  fogOBC(sh);
  Object.assign(sh.uniforms, leafU);
  sh.fragmentShader = 'uniform float uSweep, uGloss;\n' + sh.fragmentShader.replace('#include <map_fragment>', `#include <map_fragment>
  {
    vec2 q = vMapUv; float yt = 1.0 - q.y;
    float lum = dot(diffuseColor.rgb, vec3(0.299, 0.587, 0.114));
    float ink = smoothstep(0.11, 0.035, lum);       // texel values are linear here
    float xr = (0.918 - q.x) / 0.88;                 // 0 at the right end of a line, 1 at its left end
    const float L[7] = float[7](0.126, 0.256, 0.375, 0.488, 0.598, 0.706, 0.818);
    vec3 glow = vec3(0.0);
    for (int k = 0; k < 7; k++) {
      float band = 1.0 - smoothstep(0.032, 0.052, abs(yt - L[k]));
      float pk = clamp(uSweep * 7.0 - float(k), 0.0, 1.0);
      float on = step(0.0, xr) * step(xr, pk) * step(0.001, pk) * band;
      float head = exp(-pow((xr - pk) * 28.0, 2.0)) * band * step(0.001, pk) * step(pk, 0.999);
      glow += vec3(0.9, 0.08, 0.05) * ink * (on * 0.75 + head * 1.6) + vec3(1.0, 0.45, 0.3) * head * 0.06 * step(0.0, xr);
    }
    float g = (1.0 - smoothstep(0.012, 0.03, abs(yt - 0.093))) * step(0.6, q.x) * step(q.x, 0.93);
    float redInk = smoothstep(0.15, 0.3, diffuseColor.r - diffuseColor.g);
    glow += vec3(1.0, 0.3, 0.15) * redInk * g * uGloss * (0.9 + 0.6 * sin(uTime * 3.0));
    diffuseColor.rgb = diffuseColor.rgb * (1.0 - 0.6 * min(glow.r * 2.0, 1.0)) + glow;
    float e = smoothstep(0.0, 0.04, q.x) * smoothstep(1.0, 0.96, q.x) * smoothstep(0.0, 0.04, q.y) * smoothstep(1.0, 0.96, q.y);
    diffuseColor.a *= e;
  }`);
};
const leaf = new THREE.Group();
const leafMesh = new THREE.Mesh(new THREE.PlaneGeometry(LW, LH), leafMat);
leafMesh.renderOrder = 6; leaf.add(leafMesh);
const LEAF_Y = -59;

/* ------------------------------------------------------------------ scroll mapping */
// u runs 0 at the top of the page, k + 0.5 when section k is centred on screen
let anchors = [];
function measure() {
  const top0 = scrollY; anchors = [[0, 0]];
  sections.forEach((s, k) => { if (!k) return; const r = s.getBoundingClientRect(); anchors.push([r.top + top0 + r.height / 2 - innerHeight / 2, k + 0.5]); });
  const last = sections[sections.length - 1].getBoundingClientRect();
  anchors.push([last.bottom + top0 - innerHeight, sections.length]);
}
function uOf(y) {
  if (y <= anchors[0][0]) return 0;
  for (let i = 1; i < anchors.length; i++) if (y <= anchors[i][0]) { const [a, ua] = anchors[i - 1], [b, ub] = anchors[i]; return lerp(ua, ub, (y - a) / Math.max(1, b - a)); }
  return anchors[anchors.length - 1][1];
}
function yOfU(u) {
  for (let i = 1; i < anchors.length; i++) if (u <= anchors[i][1]) { const [a, ua] = anchors[i - 1], [b, ub] = anchors[i]; return lerp(a, b, (u - ua) / Math.max(1e-6, ub - ua)); }
  return anchors[anchors.length - 1][0];
}
// camera depth on the tier path: tier n fills u in [k, k+1] where k is its section index
const PATH = []; tiers.forEach(t => { PATH.push([t.k, t.y0]); }); PATH.push([tiers[tiers.length - 1].k + 1, tiers[tiers.length - 1].y1]);
const END_K = sections.length - 1; PATH.push([END_K + 1, -126]);
function camY(u) {
  if (u <= PATH[0][0]) return PATH[0][1];
  for (let i = 1; i < PATH.length; i++) if (u <= PATH[i][0]) return lerp(PATH[i - 1][1], PATH[i][1], (u - PATH[i - 1][0]) / (PATH[i][0] - PATH[i - 1][0]));
  return PATH[PATH.length - 1][1];
}
const TH0 = 0.62, THS = 0.58;
const theta = u => TH0 + Math.max(0, u - tiers[0].k) * THS;
function uOfY(y) {               // inverse of camY on the tier path
  for (let i = 1; i < PATH.length; i++) { const [ua, ya] = PATH[i - 1], [ub, yb] = PATH[i]; if (y <= ya && y >= yb) return lerp(ua, ub, (ya - y) / (ya - yb)); }
  return y > PATH[0][1] ? PATH[0][0] : PATH[PATH.length - 1][0];
}
const avgR = y => { let s = 0; for (let i = 0; i < 12; i++) s += surfR(i / 12 * Math.PI * 2, y); return s / 12; };

/* ------------------------------------------------------------------ the red thread */
const threadPts = [], HTOP = colH(TH0 + 0.16) * 0.96;
{
  for (let y = HTOP; y >= -116; y -= (y > 0 ? 0.5 : 1.2)) {
    const a = theta(uOfY(Math.min(y, 9))) + 0.16;
    threadPts.push(surfP(a, y, 0.35));
  }
}
const threadCurve = new THREE.CatmullRomCurve3(threadPts, false, 'centripetal');
const T_SEG = 900;
const threadGeo = new THREE.TubeGeometry(threadCurve, T_SEG, 0.085, 6, false);
const threadMat = patch(forceFog(new THREE.MeshBasicMaterial({ color: 0xff3b30, toneMapped: false })));
const thread = new THREE.Mesh(threadGeo, threadMat); thread.renderOrder = 2; scene.add(thread);
const threadYs = Array.from({ length: T_SEG + 1 }, (_, i) => threadCurve.getPointAt(i / T_SEG).y);
function threadTo(y) {       // draw the thread down to height y
  let i = 0; while (i < T_SEG && threadYs[i] > y) i++;
  threadGeo.setDrawRange(0, i * 6 * 6);
  return threadCurve.getPointAt(i / T_SEG);
}
const glowTex = (() => { const c = document.createElement('canvas'); c.width = c.height = 128; const x = c.getContext('2d');
  const g = x.createRadialGradient(64, 64, 0, 64, 64, 64); g.addColorStop(0, 'rgba(255,255,255,1)'); g.addColorStop(0.2, 'rgba(255,120,100,.9)'); g.addColorStop(1, 'rgba(255,40,30,0)');
  x.fillStyle = g; x.fillRect(0, 0, 128, 128); const t = new THREE.CanvasTexture(c); return t; })();
const head = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTex, blending: THREE.AdditiveBlending, depthWrite: false, toneMapped: false }));
head.scale.setScalar(2.2); scene.add(head);

/* ------------------------------------------------------------------ tier contours */
const rings = [];
tiers.slice(1).forEach(t => {
  const y = t.y0, pts = [];
  for (let i = 0; i <= 240; i++) { const a = i / 240 * Math.PI * 2; pts.push(surfP(a, y, 0.45)); }
  const line = new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts),
    patch(forceFog(new THREE.LineBasicMaterial({ color: 0xbfe9ff, transparent: true, opacity: 0.55, toneMapped: false }))));
  scene.add(line); rings.push({ line, y, t });
});

/* ------------------------------------------------------------------ props */
function canvasTex(w, h, draw) { const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; return t; }
const props = [];
function placeProp(obj, y, side, out) {        // beside the berg on the camera's path at height y
  const a = theta(uOfY(y)) + side; const r = avgR(y) + out;
  obj.position.set(Math.cos(a) * r, y, Math.sin(a) * r); obj.userData.base = obj.position.clone(); obj.userData.side = side; obj.userData.r = r;
  scene.add(obj); props.push(obj); return obj;
}
// tier 2: a scytale with its strip
{
  const g = new THREE.Group();
  const rod = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.42, 7, 24), new THREE.MeshStandardMaterial({ color: 0x7a4b2a, roughness: 0.7 }));
  const tex = canvasTex(2048, 64, (x, w, h) => { x.fillStyle = '#e8d9b5'; x.fillRect(0, 0, w, h); x.fillStyle = '#4a3220'; x.font = 'italic 40px Georgia, serif';
    const s = 'KAINOIDHMHTHRESTHSHELLADOSKAIPAIDESAUTHS'; for (let i = 0; i < 70; i++) x.fillText(s[i % s.length], 8 + i * 29, 46); });
  const strip = []; const turns = 7, N = 400;
  for (let i = 0; i <= N; i++) { const t = i / N, a = t * turns * Math.PI * 2, y = lerp(-3.1, 3.1, t);
    strip.push([Math.cos(a) * 0.45, y - 0.18, Math.sin(a) * 0.45, Math.cos(a) * 0.45, y + 0.18, Math.sin(a) * 0.45, t]); }
  const pos = [], uv = [], ix = [];
  strip.forEach(([x1, y1, z1, x2, y2, z2, t], i) => { pos.push(x1, y1, z1, x2, y2, z2); uv.push(t, 0, t, 1); if (i) { const b = i * 2; ix.push(b - 2, b, b - 1, b - 1, b, b + 1); } });
  const sg = new THREE.BufferGeometry(); sg.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); sg.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2)); sg.setIndex(ix); sg.computeVertexNormals();
  g.add(rod, new THREE.Mesh(sg, new THREE.MeshStandardMaterial({ map: tex, side: THREE.DoubleSide, roughness: 0.8 })));
  g.userData.tilt = 0.5;
  g.traverse(o => o.material && patch(forceFog(o.material)));
  placeProp(g, -7.5, -0.06, 18);
}
// tier 3: Alberti's disk
{
  const g = new THREE.Group();
  const outer = 'ABCDEFGILMNOPQRSTVXZ1234', inner = 'gklnprtvz&xysomqihfdbace';
  const ring = (letters, r0, r1, bg, ink, size) => canvasTex(1024, 1024, (x, w) => {
    const c = w / 2; x.translate(c, c);
    x.fillStyle = bg; x.beginPath(); x.arc(0, 0, r1 * c, 0, 7); x.arc(0, 0, r0 * c, 0, 7, true); x.fill();
    x.strokeStyle = ink; x.lineWidth = 3; x.beginPath(); x.arc(0, 0, r1 * c - 2, 0, 7); x.stroke(); x.beginPath(); x.arc(0, 0, r0 * c + 2, 0, 7); x.stroke();
    x.fillStyle = ink; x.font = `${size}px Georgia, serif`; x.textAlign = 'center'; x.textBaseline = 'middle';
    letters.split('').forEach((ch, i) => { const a = i / letters.length * Math.PI * 2; x.save(); x.rotate(a); x.fillText(ch, 0, -(r0 + r1) / 2 * c);
      x.restore(); x.save(); x.rotate(a + Math.PI / letters.length); x.beginPath(); x.moveTo(0, -r0 * c); x.lineTo(0, -r1 * c); x.stroke(); x.restore(); });
  });
  const mk = (tex, z) => { const m = new THREE.Mesh(new THREE.CircleGeometry(3.3, 96), patch(forceFog(new THREE.MeshBasicMaterial({ map: tex, transparent: true, side: THREE.DoubleSide, toneMapped: false }))));
    m.position.z = z; return m; };
  const o = mk(ring(outer, 0.68, 0.98, '#c9a25c', '#2b1b08', 64), 0);
  const i = mk(ring(inner, 0.3, 0.67, '#efe2c2', '#3a2410', 56), 0.03);
  const hub = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.25, 0.2, 20), patch(forceFog(new THREE.MeshBasicMaterial({ color: 0x8a6a2a, toneMapped: false }))));
  hub.rotation.x = Math.PI / 2;
  g.add(o, i, hub); g.userData.inner = i; g.userData.spin = [0, 0.12, 0];
  placeProp(g, -23, -0.03, 25);
}
// tier 4: a nomenclator leaf
{
  const tex = canvasTex(900, 1240, (x, w, h) => {
    const gr = x.createLinearGradient(0, 0, w, h); gr.addColorStop(0, '#efe1bf'); gr.addColorStop(1, '#d9c393'); x.fillStyle = gr; x.fillRect(0, 0, w, h);
    x.fillStyle = 'rgba(120,80,30,.08)'; for (let i = 0; i < 260; i++) { x.beginPath(); x.arc(Math.random() * w, Math.random() * h, Math.random() * 18, 0, 7); x.fill(); }
    x.fillStyle = '#3b2412'; x.font = 'italic 54px Georgia, serif'; x.fillText('Chiffre pour Monsieur', 120, 110);
    x.font = 'italic 34px Georgia, serif';
    const al = 'abcdefghilmnopqrstuxyz'.split('');
    al.forEach((ch, i) => { const col = i % 2, row = Math.floor(i / 2); const X = 80 + col * 380, Y = 190 + row * 50;
      x.fillText(ch, X, Y); x.fillText([12 + i * 3, 40 + i, 77 - i].slice(0, 'aeiou'.includes(ch) ? 3 : 1).join('  '), X + 50, Y); });
    x.font = 'italic 32px Georgia, serif'; x.fillText('le Pape  22      le Roy d’Espagne  Δ', 80, 800);
    x.fillText('l’Empereur  ⊕     Venise  64     la paix  318', 80, 852); x.fillText('le Duc  θ     argent  97     nulles  5  9  0', 80, 904);
    x.strokeStyle = 'rgba(59,36,18,.5)'; x.lineWidth = 2; x.strokeRect(40, 40, w - 80, h - 80);
  });
  const geo = new THREE.PlaneGeometry(4.4, 6, 20, 20); const p = geo.attributes.position;
  for (let i = 0; i < p.count; i++) p.setZ(i, Math.sin(p.getX(i) * 0.9) * 0.25 + Math.sin(p.getY(i) * 0.6) * 0.12); geo.computeVertexNormals();
  const m = new THREE.Mesh(geo, patch(forceFog(new THREE.MeshStandardMaterial({ map: tex, side: THREE.DoubleSide, roughness: 0.9, emissive: 0xffffff, emissiveMap: tex, emissiveIntensity: 0.55 }))));
  m.userData.spin = [0.02, 0.1, 0.03]; placeProp(m, -41, -0.03, 25);
}
// tier 5: sealed letters drifting down
const letters = new THREE.Group(); scene.add(letters);
{
  const tex = canvasTex(256, 170, (x, w, h) => { x.fillStyle = '#ead9b0'; x.fillRect(0, 0, w, h); x.strokeStyle = 'rgba(80,50,20,.35)'; x.lineWidth = 2;
    x.beginPath(); x.moveTo(0, 0); x.lineTo(w / 2, h * 0.55); x.lineTo(w, 0); x.stroke(); x.fillStyle = '#9c1c16'; x.beginPath(); x.arc(w / 2, h * 0.55, 20, 0, 7); x.fill();
    x.fillStyle = '#c6362c'; x.beginPath(); x.arc(w / 2 - 4, h * 0.55 - 4, 9, 0, 7); x.fill(); });
  const mat = patch(forceFog(new THREE.MeshStandardMaterial({ map: tex, side: THREE.DoubleSide, roughness: 0.85, emissive: 0xffffff, emissiveMap: tex, emissiveIntensity: 0.5 })));
  const geo = new THREE.PlaneGeometry(1.5, 1.0);
  for (let i = 0; i < (SMALL ? 14 : 24); i++) {
    const m = new THREE.Mesh(geo, mat); const y = lerp(-50, -70, Math.random()); const a = theta(uOfY(y)) + lerp(-0.9, 0.9, Math.random());
    const r = avgR(y) + lerp(4, 18, Math.random());
    m.position.set(Math.cos(a) * r, y, Math.sin(a) * r); m.rotation.set(Math.random() * 6, Math.random() * 6, Math.random() * 6);
    m.userData = { v: lerp(0.15, 0.4, Math.random()), s: [Math.random() - 0.5, Math.random() - 0.5, Math.random() - 0.5].map(v => v * 0.6), a, r };
    letters.add(m);
  }
}
// tier 6: a clay tablet
{
  const tex = canvasTex(512, 640, (x, w, h) => { x.fillStyle = '#a77b52'; x.fillRect(0, 0, w, h);
    for (let row = 0; row < 11; row++) { x.fillStyle = 'rgba(0,0,0,.08)'; x.fillRect(20, 40 + row * 54, w - 40, 2);
      for (let k = 0; k < 9; k++) { const X = 40 + k * 50 + (row % 2) * 12, Y = 62 + row * 54; x.fillStyle = 'rgba(50,25,8,.55)';
        const n = 1 + ((row * 7 + k * 3) % 3); for (let q = 0; q < n; q++) { x.beginPath(); x.moveTo(X + q * 12, Y - 12); x.lineTo(X + q * 12 + 9, Y - 12); x.lineTo(X + q * 12 + 4, Y + 10); x.fill(); } } } });
  const geo = new THREE.BoxGeometry(3.2, 4, 0.7, 6, 6, 2); const p = geo.attributes.position;
  for (let i = 0; i < p.count; i++) { const zz = p.getZ(i); p.setZ(i, zz * (1 - 0.18 * (p.getX(i) ** 2 / 2.6 + p.getY(i) ** 2 / 4))); }
  geo.computeVertexNormals();
  const m = new THREE.Mesh(geo, patch(forceFog(new THREE.MeshStandardMaterial({ map: tex, roughness: 0.95, emissive: 0xffffff, emissiveMap: tex, emissiveIntensity: 0.45 }))));
  m.userData.spin = [0.03, 0.12, 0.02]; placeProp(m, -77, -0.03, 24);
}
// tier 5: the leaf of Penn LJS 51, kept flat and readable
leaf.userData.calm = true; leaf.scale.setScalar(1.35); placeProp(leaf, LEAF_Y, 0.12, 30);
// the sea floor and one light for every open cipher
const FLOOR = -140;
{
  const g = new THREE.PlaneGeometry(900, 900, 90, 90); const p = g.attributes.position;
  for (let i = 0; i < p.count; i++) { const x = p.getX(i), y = p.getY(i); const d = Math.hypot(x, y);
    p.setZ(i, fbm(x * 0.012, y * 0.012, 2.2, 3) * 9 + Math.max(0, 22 - d) * 0.3); }
  g.computeVertexNormals();
  const f = new THREE.Mesh(g, patch(forceFog(new THREE.MeshStandardMaterial({ color: 0x5f7f8f, roughness: 1, flatShading: true }))));
  f.rotation.x = -Math.PI / 2; f.position.y = FLOOR; scene.add(f);
}
const lights = (() => {
  const n = clamp(openN, 50, 4000), pos = new Float32Array(n * 3), seed = new Float32Array(n);
  for (let i = 0; i < n; i++) { const a = Math.random() * Math.PI * 2, r = 16 + Math.pow(Math.random(), 0.7) * 150;
    const x = Math.cos(a) * r, z = Math.sin(a) * r; pos.set([x, FLOOR + fbm(x * 0.012, -z * 0.012, 2.2, 3) * 9 + 0.6, z], i * 3); seed[i] = Math.random(); }
  const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.BufferAttribute(pos, 3)); g.setAttribute('seed', new THREE.BufferAttribute(seed, 1));
  const m = new THREE.ShaderMaterial({ transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, uniforms: { ...U, uOn: { value: 0 }, uPx: { value: renderer.getPixelRatio() } },
    vertexShader: `attribute float seed; uniform float uTime, uOn, uPx; varying float vA;
      void main(){ vec4 mv = modelViewMatrix * vec4(position, 1.0); gl_Position = projectionMatrix * mv;
        float tw = 0.55 + 0.45 * sin(uTime * (0.6 + seed * 1.4) + seed * 40.0);
        vA = tw * uOn * smoothstep(0.0, 0.25, uOn - seed * 0.7); gl_PointSize = (2.0 + 5.0 * seed) * uPx * (120.0 / -mv.z); }`,
    fragmentShader: `varying float vA; void main(){ vec2 c = gl_PointCoord - 0.5; float d = length(c); float a = smoothstep(0.5, 0.0, d);
      gl_FragColor = vec4(vec3(1.0, 0.82, 0.55) * a * vA, 1.0); }` });
  const pts = new THREE.Points(g, m); scene.add(pts); return m;
})();

/* marine snow */
const snow = (() => {
  const n = SMALL ? 1400 : 2600, pos = new Float32Array(n * 3); for (let i = 0; i < n * 3; i++) pos[i] = (Math.random() - 0.5) * 110;
  const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  const m = new THREE.ShaderMaterial({ transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, uniforms: { ...U, uCam: { value: new THREE.Vector3() }, uPx: { value: renderer.getPixelRatio() } },
    vertexShader: `uniform vec3 uCam; uniform float uTime, uUnder, uPx; varying float vA;
      void main(){ vec3 p = position + vec3(sin(uTime * 0.1 + position.y) * 2.0, -uTime * 0.6, cos(uTime * 0.13 + position.x) * 2.0);
        p = mod(p - uCam + 55.0, 110.0) - 55.0 + uCam; vec4 mv = viewMatrix * vec4(p, 1.0); gl_Position = projectionMatrix * mv;
        float d = -mv.z; vA = uUnder * smoothstep(60.0, 8.0, d) * smoothstep(0.5, 3.0, d) * step(p.y, -0.5);
        gl_PointSize = uPx * 60.0 / d; }`,
    fragmentShader: `varying float vA; void main(){ float d = length(gl_PointCoord - 0.5); gl_FragColor = vec4(vec3(0.75, 0.9, 1.0) * smoothstep(0.5, 0.1, d) * vA * 0.55, 1.0); }` });
  const p = new THREE.Points(g, m); p.frustumCulled = false; scene.add(p); return m;
})();

/* god rays */
const rays = new THREE.Group(); scene.add(rays);
{
  const tex = canvasTex(64, 512, (x, w, h) => { const g = x.createLinearGradient(0, 0, 0, h); g.addColorStop(0, 'rgba(200,240,255,.55)'); g.addColorStop(1, 'rgba(200,240,255,0)');
    x.fillStyle = g; x.fillRect(0, 0, w, h); const g2 = x.createLinearGradient(0, 0, w, 0); g2.addColorStop(0, 'rgba(0,0,0,1)'); g2.addColorStop(0.5, 'rgba(0,0,0,0)'); g2.addColorStop(1, 'rgba(0,0,0,1)');
    x.globalCompositeOperation = 'destination-out'; x.fillStyle = g2; x.fillRect(0, 0, w, h); });
  tex.colorSpace = THREE.SRGBColorSpace;
  for (let i = 0; i < 9; i++) {
    const m = new THREE.Mesh(new THREE.PlaneGeometry(lerp(2, 7, Math.random()), 70), new THREE.MeshBasicMaterial({ map: tex, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide, toneMapped: false, opacity: 0.0 }));
    m.userData = { a: TH0 + 0.4 + lerp(-0.7, 0.7, Math.random()), r: lerp(16, 46, Math.random()), ph: Math.random() * 6, w: lerp(0.3, 0.8, Math.random()) };
    m.geometry.translate(0, -35, 0); rays.add(m);
  }
}

/* cipher dust: ciphertext of each tier drifting in the water */
const DUST = [
  ['PHHW PH', 'DW WKH', 'IRUXP', 'QEB NRFZH', 'BKFDJX', 'ZRCNA'],
  ['ADFGVX', 'GX AV DF', 'LXFOPV', 'EFRNHR', '0075', '13040'],
  ['gklnpr', 'tvz&xy', 'ABCDEF', '⊕ ☉ ♀', 'Ave Maria', '1 2 3 4'],
  ['972', '22  Δ', '318 64', '12 37 64', 'θ 97', '5 9 0'],
  ['NARA M34', 'fr. 2988', 'BAY → BUY', 'MANCHESTER', 'BLUFF', 'R4806'],
  ['ששך', 'בבל', 'ᚠᚢᚦᚨ', 'عمى', '+NDXOX+', 'ᚱᚲᚷ'],
  ['?', '? ? ?', '…', '?', '· · ·', '?']
];
const dust = [];
DUST.forEach((words, ti) => {
  const t = tiers[ti]; if (!t) return;
  words.forEach((w, j) => {
    const tex = canvasTex(512, 128, (x, W, H) => { x.font = '500 64px "JetBrains Mono", Consolas, monospace'; x.textAlign = 'center'; x.textBaseline = 'middle';
      x.fillStyle = ti ? 'rgba(210,240,255,.95)' : 'rgba(40,70,100,.85)'; x.fillText(w, W / 2, H / 2); });
    const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: tex, transparent: true, depthWrite: false, toneMapped: false, opacity: 0 }));
    const y = lerp(t.y0, t.y1, (j + 0.5) / words.length) + lerp(-2, 2, Math.random());
    const a = theta(uOfY(y)) + (j % 2 ? 1 : -1) * lerp(0.5, 0.95, Math.random()); const r = avgR(y) + lerp(5, 14, Math.random());
    s.position.set(Math.cos(a) * r, y, Math.sin(a) * r); s.scale.set(4, 1, 1); s.userData = { base: s.position.clone(), ph: Math.random() * 6, ti };
    scene.add(s); dust.push(s);
  });
});

/* gulls */
const gulls = (() => {
  const n = 9, g = new THREE.BufferGeometry(), pos = new Float32Array(n * 4 * 3); g.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  const idx = []; for (let i = 0; i < n; i++) idx.push(i * 4, i * 4 + 1, i * 4 + 1, i * 4 + 2, i * 4 + 2, i * 4 + 3); g.setIndex(idx);
  const l = new THREE.LineSegments(g, new THREE.LineBasicMaterial({ color: 0x3a4652, transparent: true, opacity: 0.7 })); l.frustumCulled = false; scene.add(l);
  const b = Array.from({ length: n }, () => ({ r: lerp(30, 70, Math.random()), h: lerp(20, 34, Math.random()), s: lerp(0.08, 0.16, Math.random()), p: Math.random() * 6, f: lerp(5, 8, Math.random()) }));
  return { l, pos, b };
})();

/* ------------------------------------------------------------------ labels */
const labLayer = $('#ib-labels'), leads = $('#ib-leads');
const SVGNS = 'http://www.w3.org/2000/svg';
items.forEach(it => {
  const u = it.t.k + (it.i + 0.5) / it.m;
  let y = camY(u) - 1.2 + (it.i % 2 ? 0.8 : -0.8);
  const R = avgR(Math.min(y, 1)); const side = it.i % 2 ? 1 : -1; const L = 6 + 4 * ((it.i >> 1) % 3);
  const da = Math.asin(Math.min(0.92, L / Math.max(R, 1))) * side;
  it.a = theta(u) + da; it.u = u;
  if (y > 0) y = Math.min(y, colH(it.a) * 0.8);
  it.p = surfP(it.a, y, 0.3); it.n = new THREE.Vector3(Math.cos(it.a), 0, Math.sin(it.a));
  const b = document.createElement('button'); b.type = 'button'; b.className = 'ib-lab' + (y > 0 ? ' above' : ''); b.tabIndex = -1;
  b.innerHTML = `<small>${it.yr}</small>${it.title}`; b.addEventListener('click', () => openCard(it));
  b.addEventListener('mouseenter', () => { it.hot = true; sound.tick(); }); b.addEventListener('mouseleave', () => { it.hot = false; });
  labLayer.appendChild(b); it.el = b;
  it.ln = document.createElementNS(SVGNS, 'line'); it.dot = document.createElementNS(SVGNS, 'circle'); it.dot.setAttribute('r', '3');
  leads.append(it.ln, it.dot);
  const sum = $('summary', it.li);
  sum.addEventListener('click', e => { e.preventDefault(); openCard(it); });
  sum.addEventListener('focus', () => { it.hot = true; scrollToU(it.u); });
  sum.addEventListener('blur', () => { it.hot = false; });
});

/* ------------------------------------------------------------------ card */
const card = $('#ib-card');
let cur = null;
function openCard(it, push = true) {
  cur = it; it.seen = true; it.el.classList.add('seen');
  $('#ib-card-k').textContent = `Tier ${it.t.n} · ${it.t.name} · ${it.yr}`;
  $('#ib-card-t').innerHTML = it.title;
  $('#ib-card-b').innerHTML = it.body.innerHTML;
  const k = items.indexOf(it); $('#ib-prev').disabled = k === 0; $('#ib-next').disabled = k === items.length - 1;
  card.hidden = false; card.scrollTop = 0;
  if (push) history.replaceState(null, '', '#' + it.id);
  sound.chime(it.t.n);
}
function closeCard() { card.hidden = true; cur = null; history.replaceState(null, '', location.pathname + location.search); }
$('#ib-card-x').onclick = closeCard;
$('#ib-prev').onclick = () => { const it = items[items.indexOf(cur) - 1]; if (it) { openCard(it); scrollToU(it.u); } };
$('#ib-next').onclick = () => { const it = items[items.indexOf(cur) + 1]; if (it) { openCard(it); scrollToU(it.u); } };
addEventListener('keydown', e => {
  if (card.hidden) return;
  if (e.key === 'Escape') closeCard();
  else if (e.key === 'ArrowRight' && !$('#ib-next').disabled) $('#ib-next').click();
  else if (e.key === 'ArrowLeft' && !$('#ib-prev').disabled) $('#ib-prev').click();
});
function scrollToU(u) { scrollTo({ top: yOfU(u), behavior: REDUCE ? 'auto' : 'smooth' }); }

/* ------------------------------------------------------------------ HUD */
const gl = $('#ib-gauge-list');
tiers.forEach(t => { const li = document.createElement('li'); li.innerHTML = `<a href="#${t.sec.id}">${t.name}</a>`;
  li.firstChild.addEventListener('click', e => { e.preventDefault(); scrollToU(t.k + 0.5); }); gl.appendChild(li); t.g = li; });

/* kinetic text: split the big lines into words, reveal each block as it arrives */
$$('.ib-big').forEach(p => { if (p.children.length) return; p.innerHTML = p.textContent.split(' ').map((w, i) => `<span class="w" style="transition-delay:${i * 90}ms">${w}</span>`).join(' '); });
const io = new IntersectionObserver(es => es.forEach(e => e.target.classList.toggle('in', e.isIntersecting)), { rootMargin: '-12% 0px -12% 0px' });
$$('.ib-say').forEach(s => io.observe(s));
new IntersectionObserver(es => body.classList.toggle('ib-done', es[0].isIntersecting), { rootMargin: '0px 0px -40% 0px' }).observe($('main'));

/* ------------------------------------------------------------------ sound: all synthesized */
const sound = (() => {
  let ctx = null, on = false, master, envF, gWind, gSurf, gDrone, verb, bp, lastTier = 0;
  function noiseBuf(sec) { const b = ctx.createBuffer(1, ctx.sampleRate * sec, ctx.sampleRate), d = b.getChannelData(0); let l = 0;
    for (let i = 0; i < d.length; i++) { const w = Math.random() * 2 - 1; l = (l + 0.02 * w) / 1.02; d[i] = l * 3.5 + w * 0.12; } return b; }
  function start() {
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    master = ctx.createGain(); master.gain.value = 0; master.connect(ctx.destination);
    envF = ctx.createBiquadFilter(); envF.type = 'lowpass'; envF.frequency.value = 12000; envF.connect(master);
    const n = ctx.createBufferSource(); n.buffer = noiseBuf(4); n.loop = true;
    bp = ctx.createBiquadFilter(); bp.type = 'bandpass'; bp.frequency.value = 700; bp.Q.value = 0.6;
    gWind = ctx.createGain(); gWind.gain.value = 0; n.connect(bp).connect(gWind).connect(envF);
    const n2 = ctx.createBufferSource(); n2.buffer = noiseBuf(5); n2.loop = true; const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 380;
    gSurf = ctx.createGain(); gSurf.gain.value = 0; n2.connect(lp).connect(gSurf).connect(envF);
    const lfo = ctx.createOscillator(); lfo.frequency.value = 0.09; const lg = ctx.createGain(); lg.gain.value = 0.25; lfo.connect(lg).connect(gSurf.gain);
    gDrone = ctx.createGain(); gDrone.gain.value = 0; const dl = ctx.createBiquadFilter(); dl.type = 'lowpass'; dl.frequency.value = 260; gDrone.connect(dl).connect(master);
    [[55, 'sine', 0.5], [55.35, 'sine', 0.5], [82.4, 'triangle', 0.12], [41.2, 'sine', 0.35]].forEach(([f, t, g]) => { const o = ctx.createOscillator(); o.type = t; o.frequency.value = f;
      const og = ctx.createGain(); og.gain.value = g; o.connect(og).connect(gDrone); o.start(); });
    verb = ctx.createConvolver(); const ir = ctx.createBuffer(2, ctx.sampleRate * 3.2, ctx.sampleRate);
    for (let c = 0; c < 2; c++) { const d = ir.getChannelData(c); for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / d.length, 3.2); }
    verb.buffer = ir; const vg = ctx.createGain(); vg.gain.value = 0.55; verb.connect(vg).connect(master);
    n.start(); n2.start(); lfo.start();
  }
  function set(p, v, t = 0.8) { if (ctx) p.setTargetAtTime(v, ctx.currentTime, t); }
  function blip(freq, dur, gain, type = 'sine', wet = true, glide = 0) {
    if (!on) return; const o = ctx.createOscillator(), g = ctx.createGain(); o.type = type; o.frequency.value = freq;
    if (glide) o.frequency.exponentialRampToValueAtTime(freq * glide, ctx.currentTime + dur);
    g.gain.setValueAtTime(0, ctx.currentTime); g.gain.linearRampToValueAtTime(gain, ctx.currentTime + 0.01); g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + dur);
    o.connect(g); g.connect(master); if (wet) g.connect(verb); o.start(); o.stop(ctx.currentTime + dur + 0.05);
  }
  return {
    toggle() { if (!ctx) start(); on = !on; if (ctx.state === 'suspended') ctx.resume(); set(master.gain, on ? 0.55 : 0, 0.3); return on; },
    update(y) {
      if (!ctx || !on) return; const under = y < 0, d = clamp(-y / 126, 0, 1);
      set(gWind.gain, under ? 0 : 0.22); set(gSurf.gain, under ? 0.05 * (1 - d) : 0.35); set(envF.frequency, under ? lerp(900, 220, d) : 12000, 0.5);
      set(gDrone.gain, under ? lerp(0.05, 0.22, d) : 0); set(bp.frequency, 600 + Math.sin(performance.now() / 4000) * 220, 1.5);
    },
    tier(n, y) { if (n === lastTier) return; lastTier = n; if (y < 0) { blip(lerp(1500, 520, (n - 1) / 6), 1.8, 0.18, 'sine', true); setTimeout(() => blip(lerp(1500, 520, (n - 1) / 6), 1.2, 0.05), 340); } },
    tick() { blip(2400, 0.05, 0.03, 'triangle', false); },
    chime(n) { const f = lerp(880, 440, (n - 1) / 6); blip(f, 1.4, 0.08); blip(f * 1.5, 1.1, 0.05); },
    disk() { blip(1800, 0.04, 0.025, 'square', false); },
    get on() { return on; }
  };
})();
$('#ib-sound').addEventListener('click', e => { const on = sound.toggle(); e.currentTarget.setAttribute('aria-pressed', String(on)); });

/* ------------------------------------------------------------------ frame */
const camPos = new THREE.Vector3(), camLook = new THREE.Vector3(), tmp = new THREE.Vector3(), tmp2 = new THREE.Vector3();
let W = 0, H = 0, textRight = 0, uS = 0, running = true;
function resize() {
  W = innerWidth; H = innerHeight; renderer.setSize(W, H, false); camera.aspect = W / H; camera.updateProjectionMatrix();
  leads.setAttribute('viewBox', `0 0 ${W} ${H}`);
  const say = $('.ib-tier .ib-say'); textRight = W > 760 && say ? say.getBoundingClientRect().right + 16 : 0;
  measure();
}
addEventListener('resize', resize); resize();
new ResizeObserver(() => measure()).observe($('#ib-track'));

const B0 = sections.indexOf($('#tip'));
const ESTAB = new THREE.Vector3(30, 15, 46);
let last = performance.now(), diskT = 0; const clearC = new THREE.Color();
function frame(now) {
  requestAnimationFrame(frame);
  if (!running) return;
  const dt = Math.min(0.05, (now - last) / 1000); last = now;
  const t = now / 1000; U.uTime.value = REDUCE ? 20 : t;
  const target = uOf(scrollY); uS += (target - uS) * (REDUCE ? 1 : 1 - Math.exp(-dt * 6));
  const u = uS;
  const tierK = tiers[0].k;
  // a wide shot of the berg, a swoop in to the tip, then down the tier path
  const b2 = smooth(0.25, B0 + 0.6, u);         // from the wide shot to the tip
  const b3 = smooth(B0 + 0.5, tierK + 0.25, u); // and onto the tier path
  // the leaf in the abyss: its reading runs while the camera is near it
  const nearLeaf = 1 - smooth(14, 26, Math.abs(camera.position.y - LEAF_Y));
  leafU.uSweep.value = nearLeaf > 0 ? clamp(((REDUCE ? 11 : t) % 14) / 11, 0, 1) : 0; leafU.uGloss.value = nearLeaf;
  // camera
  const ha = 0.78 + (REDUCE ? 0 : Math.sin(t * 0.05) * 0.12), portraitH = W < H ? 1.5 : 1;
  const pSlide = tmp.set(Math.cos(ha) * 64 * portraitH, 10.5, Math.sin(ha) * 64 * portraitH);
  const lSlide = tmp2.set(0, 0.5, 0);
  const ty = camY(Math.max(u, tierK)), th = theta(Math.max(u, tierK));
  const portrait = W < H ? 1.55 : 1;
  const dist = (avgR(ty - 2) + (ty > 0 ? 24 : lerp(30, 50, smooth(0, -12, ty)))) * portrait;
  const pPath = new THREE.Vector3(Math.cos(th) * dist, ty + (ty > 0 ? 2.2 : 1.5), Math.sin(th) * dist);
  const lPath = new THREE.Vector3(0, ty - 2.5 - (u > END_K ? 10 * smooth(END_K, END_K + 1, u) : 0), 0);
  const est = ESTAB.clone().multiplyScalar(portrait > 1 ? 1.35 : 1), lEst = new THREE.Vector3(0, -6, 0);
  camPos.copy(pSlide).lerp(est, b2); camLook.copy(lSlide).lerp(lEst, b2);
  camPos.lerp(pPath, b3); camLook.lerp(lPath, b3);
  if (!REDUCE) { camPos.y += Math.sin(t * 0.5) * 0.15 * b2; camPos.x += Math.sin(t * 0.31) * 0.2 * b2; }
  camera.position.copy(camPos); camera.lookAt(camLook);
  // put the berg right of the text column on wide screens
  const off = W > 760 ? -W * 0.13 : 0, offY = W > 760 ? 0 : H * 0.2;
  if (off || offY) camera.setViewOffset(W, H, off, offY, W, H); else camera.clearViewOffset();
  // underwater state
  const cy = camera.position.y, under = cy < 0, d = clamp(-cy / 130, 0, 1);
  U.uUnder.value = under ? 1 : 0;
  const fc = new THREE.Color().setRGB(lerp(0.09, 0.0, Math.pow(d, 0.6)), lerp(0.36, 0.025, Math.pow(d, 0.7)), lerp(0.46, 0.06, Math.pow(d, 0.8)), THREE.LinearSRGBColorSpace);
  U.uFogCol.value.copy(fc); U.uFogDen.value = lerp(0.018, 0.012, d);
  U.uRim.value = under ? lerp(0.35, 1.1, smooth(0, 0.6, d)) : 0;
  sky.position.copy(camera.position); foam.visible = !under;
  renderer.setClearColor(under ? clearC.setRGB(fc.r, fc.g, fc.b, THREE.SRGBColorSpace) : 0x1a1730, 1);
  hemi.intensity = under ? lerp(1.3, 0.3, d) : 1.5; sun.intensity = under ? lerp(1.8, 0.15, d) : 3.2;
  iceMat.envMapIntensity = under ? 0.12 : 0.85;
  body.classList.toggle('ib-under', under && u > 1.2);
  body.classList.toggle('ib-pre', u < B0 - 0.1);
  $('.ib-vignette').style.setProperty('--ib-vig', under ? (0.4 + d * 0.5).toFixed(2) : '0');
  // the thread grows ahead of the camera
  const yEnd = u < B0 - 0.3 ? HTOP + 1 : lerp(HTOP, ty - 9, smooth(B0 - 0.3, tierK + 0.6, u));
  const hp = threadTo(yEnd);
  thread.visible = u > B0 - 0.35; head.visible = thread.visible && u < END_K + 0.6; head.position.copy(hp);
  head.scale.setScalar(2 + Math.sin(t * 3) * 0.3);
  // props
  props.forEach(p => {             // drift beside the camera, turned towards it, rocking a little
    const ud = p.userData, a = th + ud.side, k = ud.base.x;
    p.position.set(Math.cos(a) * ud.r, ud.base.y + Math.sin(t * 0.6 + k) * 0.5, Math.sin(a) * ud.r);
    p.lookAt(camera.position.x, p.position.y, camera.position.z);
    const w = REDUCE ? 0 : ud.calm ? 0.25 : 1;
    p.rotateY(Math.sin(t * 0.31 + k) * 0.45 * w); p.rotateX(Math.sin(t * 0.23 + k) * 0.18 * w); p.rotateZ((ud.tilt || 0) + Math.sin(t * 0.19 + k) * 0.08 * w);
  });
  props.forEach(p => { if (p.userData.inner && !REDUCE) { diskT += dt; if (diskT > 1.6) { diskT = 0; p.userData.innerT = (p.userData.innerT || 0) + 1; if (Math.abs(cy + 23) < 18) sound.disk(); }
      const goal = (p.userData.innerT || 0) * Math.PI * 2 / 24; p.userData.inner.rotation.z += (goal - p.userData.inner.rotation.z) * Math.min(1, dt * 8); } });
  letters.children.forEach(m => { const ud = m.userData; if (!REDUCE) { m.position.y -= ud.v * dt; m.rotation.x += ud.s[0] * dt; m.rotation.y += ud.s[1] * dt; m.rotation.z += ud.s[2] * dt; }
    if (m.position.y < -72) { m.position.y = -48; } });
  rays.children.forEach(r => { const ud = r.userData; const a = th + (ud.a - TH0) + Math.sin(t * 0.1 + ud.ph) * 0.05; const rr = avgR(-10) + ud.r * 0.5;
    r.position.set(Math.cos(a) * rr, -0.2, Math.sin(a) * rr); r.lookAt(camera.position.x, r.position.y, camera.position.z);
    r.rotation.z = Math.sin(t * 0.2 + ud.ph) * 0.12 + 0.18;
    r.material.opacity = under ? ud.w * smooth(0, -3, cy) * (1 - smooth(-15, -70, cy)) * (0.7 + 0.3 * Math.sin(t * 0.7 + ud.ph)) : 0; });
  dust.forEach(s => { const ud = s.userData; s.position.y = ud.base.y + Math.sin(t * 0.4 + ud.ph) * 0.6; const dd = Math.abs(ud.base.y - cy);
    s.material.opacity = (ud.ti === 0 ? !under : under || ud.ti === 1) ? 0.85 * (1 - smooth(10, 22, dd)) * b3 : 0; });
  snow.uniforms.uCam.value.copy(camera.position);
  lights.uniforms.uOn.value = smooth(-95, -122, cy) * 1.7;
  // gulls over the tip
  const gp = gulls.pos; gulls.b.forEach((g, i) => { const a = t * g.s + g.p, x = Math.cos(a) * g.r, z = Math.sin(a) * g.r, y = g.h + Math.sin(t * 0.7 + g.p) * 1.5;
    const fl = Math.sin(t * g.f + g.p) * 0.5, tx = -Math.sin(a), tz = Math.cos(a), w = 0.9;
    const px = -tz, pz = tx;                  // wing axis
    gp.set([x + px * w, y + fl, z + pz * w, x + px * 0.25, y - 0.05, z + pz * 0.25, x - px * 0.25, y - 0.05, z - pz * 0.25, x - px * w, y + fl, z - pz * w], i * 12); });
  gulls.l.geometry.attributes.position.needsUpdate = true; gulls.l.visible = !under;
  rings.forEach(r => { r.line.material.opacity = 0.18 + 0.5 * (1 - smooth(4, 20, Math.abs(r.y - cy))); });

  renderer.render(scene, camera);
  labels(u, cy, b3);
  hud(u, cy);
  sound.update(cy);
}

const placed = [];
function labels(u, cy, vis) {
  const cx = new THREE.Vector3();
  placed.length = 0;
  items.forEach(it => {
    const near = Math.abs(it.u - u) < 0.6 && vis > 0.5;
    let show = 0;
    if (near) {
      cx.copy(it.p).project(camera);
      const toCam = tmp2.copy(camera.position).sub(it.p).normalize();
      const facing = it.n.dot(toCam);
      if (cx.z < 1 && Math.abs(cx.x) < 1.15 && Math.abs(cx.y) < 1.1 && facing > -0.15) {
        show = (1 - smooth(0.32, 0.58, Math.abs(it.u - u))) * smooth(-0.15, 0.2, facing) * (1 - smooth(0.85, 1.1, Math.abs(cx.y)));
        const x = (cx.x * 0.5 + 0.5) * W, y = (-cx.y * 0.5 + 0.5) * H;
        const right = it.i % 2 === 1;
        const bw = it.bw || (it.bw = it.el.offsetWidth), bh = it.bh || (it.bh = it.el.offsetHeight);
        let lx = right ? x + 46 : x - 46 - bw, ly = y - bh / 2 - 18;
        if (lx < textRight) lx = Math.max(textRight, x + 46);
        lx = clamp(lx, 8, W - bw - (W > 900 ? 190 : 12));
        for (let pass = 0; pass < 6; pass++) {      // step clear of labels already placed this frame
          const hit = placed.find(q => lx < q[0] + q[2] + 6 && lx + bw + 6 > q[0] && ly < q[1] + q[3] + 6 && ly + bh + 6 > q[1]);
          if (!hit) break; ly = hit[1] + hit[3] + 6;
        }
        if (W <= 760) ly = clamp(ly, 64, H * 0.56 - bh);
        placed.push([lx, ly, bw, bh]);
        it.el.style.transform = `translate(${lx.toFixed(1)}px,${ly.toFixed(1)}px)`;
        const ax = lx < x ? lx + bw : lx, ay = ly + bh / 2;
        it.ln.setAttribute('x1', x.toFixed(1)); it.ln.setAttribute('y1', y.toFixed(1)); it.ln.setAttribute('x2', ax.toFixed(1)); it.ln.setAttribute('y2', ay.toFixed(1));
        it.dot.setAttribute('cx', x.toFixed(1)); it.dot.setAttribute('cy', y.toFixed(1));
      }
    }
    if (show < 0.02) { if (it.vis) { it.el.style.opacity = '0'; it.el.style.pointerEvents = 'none'; it.ln.style.opacity = '0'; it.dot.style.opacity = '0'; it.vis = false; } return; }
    it.vis = true;
    it.el.style.opacity = show.toFixed(3); it.el.style.pointerEvents = show > 0.4 ? 'auto' : 'none';
    it.ln.style.opacity = (show * 0.9).toFixed(3); it.dot.style.opacity = show.toFixed(3);
    const hot = it.hot || cur === it; it.el.classList.toggle('hot', hot); it.dot.classList.toggle('hot', hot);
    it.ln.style.stroke = cy > 0 ? 'rgba(19,38,58,.5)' : ''; it.dot.style.fill = hot ? '' : (cy > 0 ? '#13263a' : '');
  });
}
let lastNo = -1, lastTierOn = null;
function hud(u, cy) {
  const k = Math.min(sections.length - 1, Math.floor(u));
  if (k !== lastNo) { $('#ib-slideno').textContent = String(k + 1); lastNo = k; }
  const t = tiers.find(t => u >= t.k && u < t.k + 1);
  if (t !== lastTierOn) { tiers.forEach(x => x.g.classList.toggle('on', x === t)); lastTierOn = t; if (t) sound.tier(t.n, cy); }
  $('#ib-gauge-fill').style.height = (clamp((u - tiers[0].k) / (tiers.length), 0, 1) * 100).toFixed(2) + '%';
  $('#ib-depth').textContent = Math.max(0, Math.round(-cy * 3.2)).toLocaleString('en');
}
document.addEventListener('visibilitychange', () => { running = !document.hidden; last = performance.now(); });
requestAnimationFrame(frame);

// a link to one entry opens it
function fromHash() { const id = location.hash.slice(1); const it = items.find(x => x.id === id);
  if (it) { measure(); scrollTo({ top: yOfU(it.u), behavior: 'auto' }); uS = it.u; setTimeout(() => openCard(it, false), 400); } }
addEventListener('load', fromHash); addEventListener('hashchange', fromHash);
}
