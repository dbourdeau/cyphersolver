"""Contrastive (SimCLR-style) glyph embedding on the v2 glyph masks. usage: python train_emb.py out.pt [epochs]"""
import sys, pickle, numpy as np, torch, torch.nn as nn, torch.nn.functional as Fn, cv2, random
torch.manual_seed(0); np.random.seed(0); random.seed(0)
pages = ['R5464_P1_0','R5464_P2_0','R5465_P1_0','R5465_P2_0','R5463_P_0','R5459_P1_0','R5460']
def prep(m, S=32):
    h, w = m.shape; side = max(h, w) + 4
    pad = np.zeros((side, side), np.uint8); pad[(side-h)//2:(side-h)//2+h, (side-w)//2:(side-w)//2+w] = m
    return cv2.resize(pad, (S, S), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
X = []; meta = []
for t in pages:
    r = pickle.load(open(f'sr_{t}/glyphs2.pkl', 'rb'))
    if t == 'R5460': r = [g for g in r if g['line'] <= 8]
    for g in r: X.append(prep(g['mask'])); meta.append((t, g['line'], g['k']))
X = torch.tensor(np.array(X))[:, None]; N = len(X); print('glyphs', N)
def aug(x):
    B = x.shape[0]
    ang = (torch.rand(B) - 0.5) * 2 * np.radians(9); sc = 1 + (torch.rand(B) - 0.5) * 0.24
    tx = (torch.rand(B) - 0.5) * 0.14; ty = (torch.rand(B) - 0.5) * 0.14; sh = (torch.rand(B) - 0.5) * 0.2
    th = torch.zeros(B, 2, 3)
    th[:, 0, 0] = torch.cos(ang) / sc; th[:, 0, 1] = -torch.sin(ang) / sc + sh; th[:, 0, 2] = tx
    th[:, 1, 0] = torch.sin(ang) / sc; th[:, 1, 1] = torch.cos(ang) / sc; th[:, 1, 2] = ty
    g = Fn.affine_grid(th, x.shape, align_corners=False); y = Fn.grid_sample(x, g, align_corners=False, padding_mode='zeros')
    # stroke thickness jitter
    k = random.choice([0, 0, 1, 2])
    if k == 1: y = Fn.max_pool2d(y, 3, 1, 1)
    if k == 2: y = -Fn.max_pool2d(-y, 3, 1, 1)
    y = y + 0.04 * torch.randn_like(y)
    return y.clamp(0, 1)
class Enc(nn.Module):
    def __init__(s):
        super().__init__()
        def blk(i, o): return nn.Sequential(nn.Conv2d(i, o, 3, padding=1), nn.BatchNorm2d(o), nn.ReLU(), nn.Conv2d(o, o, 3, padding=1), nn.BatchNorm2d(o), nn.ReLU(), nn.MaxPool2d(2))
        s.f = nn.Sequential(blk(1, 32), blk(32, 64), blk(64, 128), nn.AdaptiveAvgPool2d(2), nn.Flatten())
        s.emb = nn.Linear(512, 128); s.proj = nn.Sequential(nn.ReLU(), nn.Linear(128, 64))
    def forward(s, x, proj=False):
        e = s.emb(s.f(x)); return s.proj(e) if proj else e
net = Enc(); opt = torch.optim.Adam(net.parameters(), 2e-3, weight_decay=1e-5)
epochs = int(sys.argv[2]) if len(sys.argv) > 2 else 40; B = 256
for ep in range(epochs):
    perm = torch.randperm(N); tot = 0; n = 0
    for i in range(0, N - B + 1, B):
        xb = X[perm[i:i+B]]; z1 = Fn.normalize(net(aug(xb), True), dim=1); z2 = Fn.normalize(net(aug(xb), True), dim=1)
        sim = torch.cat([z1, z2]) @ torch.cat([z1, z2]).T / 0.2
        sim.fill_diagonal_(-1e9)
        tgt = torch.cat([torch.arange(B, 2 * B), torch.arange(0, B)])
        loss = Fn.cross_entropy(sim, tgt); opt.zero_grad(); loss.backward(); opt.step(); tot += loss.item(); n += 1
    if ep % 5 == 0 or ep == epochs - 1: print('epoch', ep, 'loss', round(tot / n, 3), flush=True)
net.eval()
with torch.no_grad(): E = torch.cat([net(X[i:i+512]) for i in range(0, N, 512)]).numpy()
pickle.dump((meta, E), open(sys.argv[1], 'wb')); print('saved', E.shape)
