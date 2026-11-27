// LJS 51 in 3D: a page-turnable model of the codex built from the OPenn photographs.
// An Arabic codex: the front cover has its spine on the right, unread leaves lie on the
// left, and each leaf turns from left to right.
//
// The binding is modelled, not measured. The spine is a strip whose length is the thickness
// of the book. Closed, it stands upright beside the text block; opened, it lies flat on the
// table under the gutter. Every leaf is sewn to the spine at its own place along the strip,
// so in an open book the leaves come out of the gutter and curve up to the top of their pile.
// The boards hinge on the two ends of the strip.
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/OrbitControls.js';

const params = new URLSearchParams(location.search);
const EMBED = params.has('embed');
if (EMBED) document.body.classList.add('embed');
const pages = await (await fetch('pages.json')).json();   // 225 images; the last is the spine
const spineImg = pages.pop();
const N = pages.length / 2;                                // 112 leaves; 0 and N-1 are the boards
const leaves = [];
for (let k = 0; k < N; k++) leaves.push({ front: pages[2*k], back: pages[2*k+1] });

// ---- dimensions (text-block height = 1) -------------------------------------------------
const W = 0.777, H = 1.0;          // text block
const OV = 0.014;                  // board overhang beyond the text block
const BT = 0.014;                  // board thickness
const PAGES_T = 0.13;              // thickness of the 110 paper leaves together
const D = PAGES_T / (N - 2);
const NU = 48;                     // segments across a leaf
const WB = W + OV;                 // board width
const isBoard = i => i === 0 || i === N - 1;
const th = leaves.map((_, i) => isBoard(i) ? BT : D);
const pre = [0]; for (let i = 0; i < N; i++) pre.push(pre[i] + th[i]);   // pre[i] = sum th[0..i-1]
const TOTAL = pre[N];
const hL = i => TOTAL - pre[i];    // top of leaf i in the left-hand pile
const hR = i => pre[i + 1];        // top of leaf i in the right-hand pile
const uOf = i => (pre[i] + th[i] / 2) / TOTAL;   // where leaf i is sewn along the spine (0 = front board)

// ---- renderer ------------------------------------------------------------------------------
const host = document.getElementById('book3d') || document.body;
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
host.prepend(renderer.domElement);
const maxAniso = renderer.capabilities.getMaxAnisotropy();
const size = () => ({ w: host.clientWidth || innerWidth, h: host.clientHeight || innerHeight });

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x14110e);
scene.fog = new THREE.Fog(0x14110e, 4.5, 10);
const camera = new THREE.PerspectiveCamera(32, 1, 0.05, 30);
const HOME = { pos: new THREE.Vector3(0, 2.5, 1.75), target: new THREE.Vector3(0, 0, 0.06) };

scene.add(new THREE.HemisphereLight(0xfff4e0, 0x2a2018, 0.85));
const sun = new THREE.DirectionalLight(0xfff1dc, 2.2);
sun.position.set(-1.2, 3.2, 1.6);
sun.castShadow = true;
sun.shadow.mapSize.set(2048, 2048);
Object.assign(sun.shadow.camera, { left: -1.7, right: 1.7, top: 1.7, bottom: -1.7, near: 0.5, far: 8 });
sun.shadow.bias = -0.0004; sun.shadow.normalBias = 0.01;
scene.add(sun);
const fill = new THREE.DirectionalLight(0xd8e4ff, 0.35); fill.position.set(2, 1.5, -1); scene.add(fill);

const table = new THREE.Mesh(new THREE.CircleGeometry(6, 64),
  new THREE.MeshStandardMaterial({ color: 0x2b2119, roughness: 0.92 }));
table.rotation.x = -Math.PI / 2; table.position.y = -0.0005; table.receiveShadow = true;
scene.add(table);
const book = new THREE.Group(); scene.add(book);

// ---- textures ---------------------------------------------------------------------------------
const loader = new THREE.TextureLoader();
const texCache = new Map();
let onFirst = () => { const l = document.getElementById('loading'); if (l) { l.style.opacity = 0; setTimeout(() => l.remove(), 600); } onFirst = () => {}; };
function tex(id, mirrored) {
  const key = id + (mirrored ? ':m' : '');
  if (texCache.has(key)) return texCache.get(key);
  const t = loader.load(`pages/${id}.jpg`, () => onFirst());
  t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = maxAniso;
  if (mirrored) { t.wrapS = THREE.RepeatWrapping; t.repeat.x = -1; t.offset.x = 1; }
  texCache.set(key, t); return t;
}
function dropTex(id, mirrored) {
  const key = id + (mirrored ? ':m' : ''); const t = texCache.get(key);
  if (t) { t.dispose(); texCache.delete(key); }
}
// Page edges: one line per leaf, uneven in tone. Laid along v (caps) or u (side walls);
// texture coordinates are in model units, so 0.6 units of height hold all 512 lines.
function edgeTexture(alongU) {
  const c = document.createElement('canvas'); c.width = alongU ? 512 : 8; c.height = alongU ? 8 : 512;
  const g = c.getContext('2d');
  for (let k = 0; k < 512; k++) {
    const v = 172 + Math.random() * 34 - (Math.random() < 0.12 ? 38 : 0);
    g.fillStyle = `rgb(${v},${v * 0.9 | 0},${v * 0.72 | 0})`;
    alongU ? g.fillRect(k, 0, 1, 8) : g.fillRect(0, 511 - k, 8, 1);
  }
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace;
  t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = maxAniso;
  return t;
}
const capMat = new THREE.MeshStandardMaterial({ map: edgeTexture(false), roughness: 0.95 });
capMat.map.repeat.set(1, 1 / 0.6);
const wallMat = new THREE.MeshStandardMaterial({ map: edgeTexture(true), roughness: 0.95 });
wallMat.map.repeat.set(1 / 0.6, 1);
const boardEdgeMat = new THREE.MeshStandardMaterial({ color: 0x4a3426, roughness: 0.8 });

// ---- the spine ------------------------------------------------------------------------------------
// f: share of the book's thickness lying on the right (moving leaves count in part).
// open: 0 while the book is closed, 1 once it is opened past the boards.
const smooth = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
const SP = { f: 0, open: 0, right: false };
function updateSpineState() {
  let s = 0; for (const L of leaves) s += th[L.i] * L.t;
  SP.f = s / TOTAL;
  SP.right = SP.f > 0.5;
  SP.open = smooth(0, 0.11, Math.min(SP.f, 1 - SP.f));
}
const BULGE = 0.022;
// outer surface of the spine at u (0 = front-board end, 1 = back-board end)
function spinePoint(u, out = { x: 0, y: 0 }) {
  const w = Math.sin(Math.PI * u), o = SP.open;
  const cx = SP.right ? -BULGE * w : BULGE * w;
  const cy = SP.right ? TOTAL * u : TOTAL * (1 - u);
  const fx = (SP.f - u) * TOTAL, fy = 0;
  out.x = cx + (fx - cx) * o; out.y = cy + (fy - cy) * o;
  return out;
}
// where leaf i leaves the spine: one board thickness inside the outer surface
function attach(i, out = { x: 0, y: 0 }) {
  spinePoint(uOf(i), out);
  const o = SP.open, ix = (SP.right ? 1 : -1) * (1 - o), iy = o, n = Math.hypot(ix, iy) || 1;
  out.x += ix / n * BT * 0.9; out.y += iy / n * BT * 0.9;
  return out;
}

// ---- how a leaf lies -----------------------------------------------------------------------------
// A leaf is a strip of length W, its direction phi(s) at distance s from the spine.
// At rest on a pile it climbs (or drops) from where it is sewn to the top of the pile over a
// gutter length G, then lies flat: phi = PI - a*(1 - s/G)^2 on the left, a*(1 - s/G)^2 on the right.
const climbCache = new Map();
function climb(delta) {
  const key = Math.round(delta * 1e5);
  if (climbCache.has(key)) return climbCache.get(key);
  const G = Math.min(0.46, Math.max(0.05, Math.abs(delta) * 2.6));
  const rise = a => { let r = 0; for (let k = 0; k < 24; k++) { const u = (k + 0.5) / 24; r += Math.sin(a * (1 - u) * (1 - u)); } return r / 24 * G; };
  let lo = -1.45, hi = 1.45;
  for (let it = 0; it < 26; it++) { const m = (lo + hi) / 2; rise(m) < delta ? lo = m : hi = m; }
  const r = { a: (lo + hi) / 2, G };
  if (climbCache.size > 20000) climbCache.clear();
  climbCache.set(key, r); return r;
}
const P0 = { x: 0, y: 0 };
// fills xs/ys (NU+1 points) for leaf i at turn t; dir is the turning direction (curl)
function leafProfile(i, t, dir, xs, ys, drop = 0) {
  const a0 = attach(i, P0), x0 = a0.x, y0 = a0.y;
  const cl = climb(hL(i) - drop - y0), cr = climb(hR(i) - drop - y0);
  const k = 0.75 * Math.sin(Math.PI * t) * dir;          // the free edge lags behind the motion
  const ds = W / NU;
  let x = x0, y = y0; xs[0] = x; ys[0] = y;
  for (let j = 1; j <= NU; j++) {
    const s = (j - 0.5) * ds, sn = s / W;
    const wl = Math.max(0, 1 - s / cl.G) ** 2, wr = Math.max(0, 1 - s / cr.G) ** 2;
    const phi = Math.PI * (1 - t) + k * sn * sn - (1 - t) * cl.a * wl + t * cr.a * wr;
    x += Math.cos(phi) * ds; y += Math.sin(phi) * ds;
    xs[j] = x; ys[j] = y;
  }
}

// ---- paper leaves -----------------------------------------------------------------------------------
function makeLeafGeometry() {
  const g = new THREE.BufferGeometry();
  const pos = new Float32Array((NU + 1) * 2 * 3), uv = new Float32Array((NU + 1) * 2 * 2), idx = [];
  for (let i = 0; i <= NU; i++) for (let j = 0; j < 2; j++) {
    const v = i * 2 + j; uv[v*2] = 1 - i / NU; uv[v*2+1] = j === 0 ? 1 : 0;
  }
  for (let i = 0; i < NU; i++) { const a = i*2, b = a + 2, c = a + 1, d = a + 3; idx.push(a, b, c, b, d, c); }
  g.setIndex(idx);
  g.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  g.setAttribute('uv', new THREE.BufferAttribute(uv, 2));
  return g;
}
const pageMat = side => new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.88, side,
  polygonOffset: true, polygonOffsetFactor: -1, polygonOffsetUnits: -1 });
const XS = new Float32Array(NU + 1), YS = new Float32Array(NU + 1);
function shapePaper(L) {
  leafProfile(L.i, L.t, L.dir, XS, YS);
  const p = L.geo.attributes.position.array;
  for (let i = 0; i <= NU; i++) for (let j = 0; j < 2; j++) {
    const v = (i*2 + j) * 3; p[v] = XS[i]; p[v+1] = YS[i]; p[v+2] = j === 0 ? -H/2 : H/2;
  }
  L.geo.attributes.position.needsUpdate = true;
  L.geo.computeVertexNormals(); L.geo.computeBoundingSphere();
}

// ---- boards: rigid, hinged on the ends of the spine ---------------------------------------------------
// Local frame: hinge at the origin, board towards -x, its "front" image on y = 0, "back" on y = -BT.
// The front board's origin is its outer face (the cover); the back board's is its inner face.
function makeBoard(L) {
  const g = new THREE.Group(), bh = H + 2 * OV;
  const box = new THREE.Mesh(new THREE.BoxGeometry(WB, BT * 0.96, bh), boardEdgeMat);
  box.position.set(-WB / 2, -BT / 2, 0); box.castShadow = box.receiveShadow = true;
  const topG = new THREE.PlaneGeometry(WB, bh); topG.rotateX(-Math.PI / 2);
  const botG = new THREE.PlaneGeometry(WB, bh); botG.rotateZ(Math.PI); botG.rotateX(Math.PI / 2);
  L.frontMat = new THREE.MeshStandardMaterial({ roughness: 0.8 });
  L.backMat = new THREE.MeshStandardMaterial({ roughness: 0.85 });
  const top = new THREE.Mesh(topG, L.frontMat), bot = new THREE.Mesh(botG, L.backMat);
  top.position.set(-WB / 2, 0.0004, 0); bot.position.set(-WB / 2, -BT - 0.0004, 0);
  top.receiveShadow = bot.receiveShadow = true;
  g.add(box, top, bot);
  L.pick = [box, top, bot];
  for (const m of L.pick) m.userData.leaf = L;
  return g;
}
const asinC = v => Math.asin(Math.max(-1, Math.min(1, v)));
function shapeBoard(L) {
  const front = L.i === 0;
  const end = spinePoint(front ? 0 : 1, { x: 0, y: 0 });           // outer face at the spine end
  // outer face height when resting on each side
  const yLeft = front ? TOTAL : 0, yRight = front ? 0 : TOTAL;
  const phiL = Math.PI - asinC((yLeft - end.y) / WB), phiR = asinC((yRight - end.y) / WB);
  const phi = phiL + (phiR - phiL) * L.t, r = phi - Math.PI;
  if (front) L.group.position.set(end.x, end.y, 0);
  else L.group.position.set(end.x - BT * Math.sin(r), end.y + BT * Math.cos(r), 0);
  L.group.rotation.z = r;
}

for (let i = 0; i < N; i++) {
  const L = leaves[i];
  Object.assign(L, { i, t: 0, dir: 1, anim: null, board: isBoard(i) });
  if (L.board) {
    L.group = makeBoard(L);
    L.frontMat.map = tex(L.front.id, false); L.backMat.map = tex(L.back.id, false);
    L.dressed = true;
    L.shape = () => shapeBoard(L);
  } else {
    L.geo = makeLeafGeometry();
    L.frontMat = pageMat(THREE.FrontSide); L.frontMat.shadowSide = THREE.DoubleSide;
    L.backMat = pageMat(THREE.BackSide);
    const f = new THREE.Mesh(L.geo, L.frontMat), b = new THREE.Mesh(L.geo, L.backMat);
    f.castShadow = true; f.receiveShadow = b.receiveShadow = true;
    f.userData.leaf = b.userData.leaf = L; L.pick = [f, b];
    L.group = new THREE.Group(); L.group.add(f, b); L.group.visible = false;
    L.shape = () => shapePaper(L);
  }
  book.add(L.group);
}
function dress(L) {
  if (L.dressed) return;
  L.frontMat.map = tex(L.front.id, false); L.backMat.map = tex(L.back.id, true);
  L.frontMat.needsUpdate = L.backMat.needsUpdate = true; L.dressed = true;
}
function undress(L) {
  if (!L.dressed || L.board) return;
  dropTex(L.front.id, false); dropTex(L.back.id, true);
  L.frontMat.map = L.backMat.map = null; L.frontMat.needsUpdate = L.backMat.needsUpdate = true; L.dressed = false;
}

// ---- the two piles of resting leaves, as solids shaped like the fan of leaves ---------------------
// Built from the leaves themselves: rows are sampled leaves, each following its own curve, so
// the lines on the head, tail and fore-edge bend with the pages. v counts leaves (one line each).
const plainMat = new THREE.MeshStandardMaterial({ color: 0xb9a582, roughness: 0.95, side: THREE.DoubleSide });
capMat.side = wallMat.side = THREE.DoubleSide;
const ROWS = 20;
const RX = Array.from({ length: ROWS + 1 }, () => new Float32Array(NU + 1));
const RY = Array.from({ length: ROWS + 1 }, () => new Float32Array(NU + 1));
const RV = new Float32Array(ROWS + 1);
function makePile() {
  const m = new THREE.Mesh(new THREE.BufferGeometry(), [capMat, wallMat, plainMat]);
  m.castShadow = m.receiveShadow = true; book.add(m); return m;
}
const pileL = makePile(), pileR = makePile();
function setPile(m, top, bottom, t) {
  if (top === null || (t === 0 ? top > bottom : top < bottom)) { m.visible = false; return; }
  m.visible = true;
  const n = Math.abs(bottom - top), rows = Math.max(1, Math.min(ROWS, n));
  // row 0 = bottom leaf, row `rows` = top leaf (lowered so the drawn top leaf lies on it)
  for (let r = 0; r <= rows; r++) {
    const k = Math.round(n * r / rows), i = bottom + (top < bottom ? -k : k);
    leafProfile(i, t, 1, RX[r], RY[r], D * 0.6 + (r === 0 ? D * 0.4 : 0));
    RV[r] = k * D;
  }
  const pos = [], uv = [], groups = [[], [], []];
  const z0 = -(H - 0.006) / 2, z1 = -z0;
  const quad = (g, a, b, c, d) => {             // a b c d: four [x,y,z,u,v] corners
    const base = pos.length / 3;
    for (const p of [a, b, c, d]) { pos.push(p[0], p[1], p[2]); uv.push(p[3], p[4]); }
    groups[g].push(base, base + 1, base + 2, base + 1, base + 3, base + 2);
  };
  for (let r = 0; r < rows; r++) for (let j = 0; j < NU; j++) for (const z of [z0, z1]) {
    // head and tail: lines along each leaf
    quad(0, [RX[r][j], RY[r][j], z, RX[r][j], RV[r]], [RX[r][j+1], RY[r][j+1], z, RX[r][j+1], RV[r]],
            [RX[r+1][j], RY[r+1][j], z, RX[r+1][j], RV[r+1]], [RX[r+1][j+1], RY[r+1][j+1], z, RX[r+1][j+1], RV[r+1]]);
  }
  for (let r = 0; r < rows; r++) for (const j of [0, NU]) {
    // fore-edge (j = NU) and the sewn edge (j = 0)
    quad(1, [RX[r][j], RY[r][j], z0, RV[r], 0], [RX[r+1][j], RY[r+1][j], z0, RV[r+1], 0],
            [RX[r][j], RY[r][j], z1, RV[r], 1], [RX[r+1][j], RY[r+1][j], z1, RV[r+1], 1]);
  }
  for (const r of [0, rows]) for (let j = 0; j < NU; j++) {
    quad(2, [RX[r][j], RY[r][j], z0, 0, 0], [RX[r][j+1], RY[r][j+1], z0, 0, 0],
            [RX[r][j], RY[r][j], z1, 0, 0], [RX[r][j+1], RY[r][j+1], z1, 0, 0]);
  }
  const idx = [...groups[0], ...groups[1], ...groups[2]];
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
  g.setIndex(idx);
  g.addGroup(0, groups[0].length, 0);
  g.addGroup(groups[0].length, groups[1].length, 1);
  g.addGroup(groups[0].length + groups[1].length, groups[2].length, 2);
  g.computeVertexNormals();
  m.geometry.dispose(); m.geometry = g;
}

// ---- spine strip -----------------------------------------------------------------------------------
const NS = 32;
const spineGeo = (() => {
  const g = new THREE.BufferGeometry();
  const pos = new Float32Array((NS + 1) * 2 * 3), uv = new Float32Array((NS + 1) * 2 * 2), idx = [];
  for (let i = 0; i <= NS; i++) for (let j = 0; j < 2; j++) { const v = i*2 + j; uv[v*2] = i / NS; uv[v*2+1] = j === 0 ? 1 : 0; }
  for (let i = 0; i < NS; i++) { const a = i*2, b = a + 2, c = a + 1, d = a + 3; idx.push(a, c, b, b, c, d); }
  g.setIndex(idx);
  g.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  g.setAttribute('uv', new THREE.BufferAttribute(uv, 2));
  return g;
})();
const spine = new THREE.Mesh(spineGeo, new THREE.MeshStandardMaterial({ map: tex(spineImg.id, false), roughness: 0.75, side: THREE.DoubleSide }));
spine.castShadow = true; spine.receiveShadow = true; book.add(spine);
function shapeSpine() {
  const p = spineGeo.attributes.position.array, z = H / 2 + OV, q = { x: 0, y: 0 };
  for (let i = 0; i <= NS; i++) {
    spinePoint(i / NS, q);
    for (let j = 0; j < 2; j++) { const v = (i*2 + j) * 3; p[v] = q.x; p[v+1] = Math.max(q.y, 0.0003); p[v+2] = j === 0 ? -z : z; }
  }
  spineGeo.attributes.position.needsUpdate = true;
  spineGeo.computeVertexNormals(); spineGeo.computeBoundingSphere();
}

// ---- state -----------------------------------------------------------------------------------------
const goal = L => L.anim ? L.anim.to : L.t;
const moving = L => !!L.anim || !!L.dragging;
const turnedCount = () => leaves.reduce((n, L) => n + (goal(L) > 0.5 ? 1 : 0), 0);
let current = 0, lTop = null, rTop = null;

function refresh() {
  current = turnedCount();
  lTop = null; rTop = null;
  for (let i = 1; i < N - 1; i++) if (!moving(leaves[i]) && leaves[i].t === 0) { lTop = i; break; }
  for (let i = N - 2; i >= 1; i--) if (!moving(leaves[i]) && leaves[i].t === 1) { rTop = i; break; }
  for (const L of leaves) if (!L.board) L.group.visible = moving(L) || L.i === lTop || L.i === rTop;
  for (const L of leaves) {
    if (L.board) continue;
    if (Math.abs(L.i - current) <= 3 || L.group.visible) dress(L);
    else if (Math.abs(L.i - current) > 8) undress(L);
  }
  updateUI();
}
// everything that depends on the spine is reshaped together
function reshapeAll() {
  updateSpineState();
  for (const L of leaves) if (L.board || L.group.visible) L.shape();
  setPile(pileL, lTop, N - 2, 0);
  setPile(pileR, rTop, 1, 1);
  shapeSpine();
}

const ease = x => x < 0.5 ? 4*x*x*x : 1 - Math.pow(-2*x + 2, 3) / 2;
function turn(L, to) {
  if (goal(L) === to) return;
  L.dir = to > L.t ? 1 : -1;
  L.anim = { from: L.t, to, start: performance.now(), dur: (L.board ? 1150 : 950) * Math.max(0.25, Math.abs(to - L.t)) };
  refresh(); dirty = true;
}
function forward() { const L = leaves.find(L => goal(L) === 0); if (L) turn(L, 1); }
function backward() { for (let i = N - 1; i >= 0; i--) if (goal(leaves[i]) === 1) return turn(leaves[i], 0); }
let jumpTimer = null;
function setOpening(c) {
  for (const L of leaves) { L.anim = null; L.t = L.i < c ? 1 : 0; }
  refresh(); dirty = true;
}
function goTo(target) {
  clearInterval(jumpTimer);
  const diff = target - turnedCount();
  if (Math.abs(diff) > 10) setOpening(target - Math.sign(diff) * 2);
  jumpTimer = setInterval(() => {
    const c = turnedCount();
    if (c === target) return clearInterval(jumpTimer);
    c < target ? forward() : backward();
  }, 110);
}

// ---- UI ------------------------------------------------------------------------------------------------
const $ = id => document.getElementById(id);
const slider = $('slider'); slider.max = N;
function updateUI() {
  const c = current;
  $('lblL').textContent = c < N ? `left: ${leaves[c].front.label}` : '';
  $('lblR').textContent = c > 0 ? `right: ${leaves[c-1].back.label}` : '';
  $('lblMid').textContent = c === 0 ? 'Closed · front cover' : c === N ? 'Closed · back cover' : `opening ${c} of ${N - 1}`;
  if (document.activeElement !== slider) slider.value = c;
  $('fwd').disabled = c >= N; $('back').disabled = c <= 0;
}
$('fwd').onclick = forward; $('back').onclick = backward;
slider.oninput = () => goTo(+slider.value);
addEventListener('keydown', e => {
  if (e.key === 'ArrowLeft') { forward(); e.preventDefault(); }
  else if (e.key === 'ArrowRight') { backward(); e.preventDefault(); }
  else if (e.key === 'Home') { goTo(0); e.preventDefault(); }
  else if (e.key === 'End') { goTo(N); e.preventDefault(); }
});

// ---- pointer: drag a page to turn it, drag elsewhere to orbit -------------------------------------------
const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
const plane = new THREE.Plane(new THREE.Vector3(0, 1, 0), -0.05);
let drag = null, dirty = true;
function setRay(e) {
  const r = renderer.domElement.getBoundingClientRect();
  ndc.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
  ray.setFromCamera(ndc, camera);
}
const worldX = e => { setRay(e); const p = ray.ray.intersectPlane(plane, new THREE.Vector3()); return p ? p.x - book.position.x : null; };
const el = renderer.domElement;
el.addEventListener('pointerdown', e => {
  if (e.button !== 0) return;
  setRay(e);
  const meshes = leaves.filter(L => L.group.visible && !L.anim).flatMap(L => L.pick);
  const hit = ray.intersectObjects(meshes, false)[0];
  if (!hit) return;
  const L = hit.object.userData.leaf, x0 = worldX(e);
  if (x0 === null) return;
  const top = L.t === 0 ? leaves.find(l => goal(l) === 0) : [...leaves].reverse().find(l => goal(l) === 1);
  if (top !== L) return;                                   // only the top leaf of a pile can be lifted
  drag = { L, x0, t0: L.t, sx: e.clientX, sy: e.clientY, moved: false, id: e.pointerId };
  L.dragging = true; refresh(); dirty = true;
  el.setPointerCapture(e.pointerId);
  e.stopImmediatePropagation();
}, true);
el.addEventListener('pointermove', e => {
  if (!drag || e.pointerId !== drag.id) return;
  if (Math.hypot(e.clientX - drag.sx, e.clientY - drag.sy) > 5) drag.moved = true;
  const x = worldX(e); if (x === null) return;
  const span = 2 * Math.max(Math.abs(drag.x0), 0.25);
  const t = Math.min(1, Math.max(0, drag.t0 + (x - drag.x0) / span));
  drag.L.dir = t >= drag.L.t ? 1 : -1; drag.L.t = t; dirty = true;
  e.stopImmediatePropagation();
}, true);
function endDrag(e) {
  if (!drag || e.pointerId !== drag.id) return;
  const L = drag.L, to = drag.moved ? (L.t > 0.5 ? 1 : 0) : (drag.t0 > 0.5 ? 0 : 1);
  if (!drag.moved) L.dir = to > L.t ? 1 : -1;
  drag = null; L.dragging = false;
  L.anim = { from: L.t, to, start: performance.now(), dur: 950 * Math.max(0.25, Math.abs(to - L.t)) };
  refresh(); dirty = true;
  e.stopImmediatePropagation();
}
el.addEventListener('pointerup', endDrag, true);
el.addEventListener('pointercancel', endDrag, true);

const controls = new OrbitControls(camera, el);
controls.enableDamping = true; controls.dampingFactor = 0.08;
controls.minDistance = 0.5; controls.maxDistance = 5.5;
controls.maxPolarAngle = Math.PI * 0.49;
if (EMBED) controls.enableZoom = false;   // inside a page the wheel scrolls the page; zoom with the buttons
function resetView() { camera.position.copy(HOME.pos); controls.target.copy(HOME.target); controls.update(); }
if ($('reset')) $('reset').onclick = resetView;
if ($('zin')) $('zin').onclick = () => { camera.position.lerp(controls.target, 0.2); };
if ($('zout')) $('zout').onclick = () => { camera.position.sub(controls.target).multiplyScalar(1.25).add(controls.target); };

function resize() {
  const { w, h } = size();
  camera.aspect = w / h; camera.updateProjectionMatrix(); renderer.setSize(w, h, false);
  renderer.domElement.style.width = '100%'; renderer.domElement.style.height = '100%';
  if (w / h < 1) HOME.pos.set(0, 3.4, 2.3); else HOME.pos.set(0, 2.5, 1.75);
}
new ResizeObserver(resize).observe(host === document.body ? document.documentElement : host);
resize(); resetView();
window.__b = { camera, controls, goTo, setOpening };   // for inspection from the console

// opening to start at (?open=N: N leaves already turned)
const OPEN = Math.max(0, Math.min(N, parseInt(params.get('open') || '0', 10) || 0));
setOpening(OPEN);
book.position.x = OPEN === 0 ? W / 2 : OPEN === N ? -W / 2 : 0;

// ---- loop ---------------------------------------------------------------------------------------------
let onScreen = true;
new IntersectionObserver(es => { onScreen = es[0].isIntersecting; }).observe(el);
function frame(now) {
  requestAnimationFrame(frame);
  if (!onScreen) return;
  let settled = false;
  for (const L of leaves) {
    if (!L.anim || L.dragging) continue;
    const a = L.anim, x = Math.min(1, (now - a.start) / a.dur);
    L.t = a.from + (a.to - a.from) * ease(x);
    if (x >= 1) { L.t = a.to; L.anim = null; settled = true; }
    dirty = true;
  }
  if (settled) refresh();
  if (dirty) { reshapeAll(); dirty = false; }
  const c = turnedCount(), goalX = c === 0 ? W / 2 : c === N ? -W / 2 : 0;
  book.position.x += (goalX - book.position.x) * 0.08;
  controls.update();
  renderer.render(scene, camera);
}
requestAnimationFrame(frame);
