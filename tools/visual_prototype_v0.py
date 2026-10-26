"""v0: left 2/3 verse card + right 1/3 drawing (01 stages). 1920x1080."""
import cv2, glob, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, '/root/sleepdraw')
from progressive_journey import diff_mask, component_order, reveal_frame

STAGES_DIR = '/root/sleepdraw/storyboards'
PREFIX = '01-stage'
W, H = 1920, 1080
LEFT_W = 1280
RIGHT_W = 640
FPS = 15

def load_stages():
    files = sorted(glob.glob(os.path.join(STAGES_DIR, PREFIX + '-*.png')))
    return [cv2.imread(f, cv2.IMREAD_COLOR) for f in files]

def make_left_card():
    img = Image.new('RGB', (LEFT_W, H), (247, 242, 232))
    d = ImageDraw.Draw(img)
    def text(xy, s, size=48, fill=(30, 30, 30)):
        try:
            fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', size)
        except Exception:
            fnt = ImageFont.load_default()
        d.text(xy, s, font=fnt, fill=fill)
    text((80, 60), 'SIVA SUTRAS  |  S1-1 / 77', 28, (120, 90, 60))
    text((80, 130), 'Caitanyam atma', 96, (25, 25, 25))
    text((80, 260), 'Consciousness is the Self.', 54, (60, 60, 60))
    text((80, 350), 'Dyczkowski, Aphorisms of Siva', 32, (110, 110, 110))
    d.line([(80, 430), (LEFT_W - 80, 430)], fill=(200, 180, 150), width=2)
    text((80, 460), 'PLAIN', 28, (120, 90, 60))
    text((80, 500), 'consciousness is the self', 48, (40, 40, 40))
    text((80, 600), 'BAUMER (ss3-10)', 28, (120, 90, 60))
    q = '"...universal consciousness... not something\nyou are doing -- it is something which is there."'
    text((80, 640), q, 38, (50, 50, 50))
    text((80, H - 160), '[ BELL ]  Q > SANSKRIT > TRANSLATION > PLAIN > BAUMER', 26, (140, 130, 115))
    text((80, H - 110), 'TRACK F  |  B1 chant > B2 readout > B3 > B4', 26, (140, 130, 115))
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def build_right_frames(stages, frames_per_trans=12):
    out = []
    for _ in range(15):
        out.append(stages[0])
    for i in range(1, len(stages)):
        base, tgt = stages[i - 1], stages[i]
        mask = diff_mask(base, tgt)
        comps = component_order(mask)
        part = np.zeros(mask.shape, dtype=bool)
        for t in range(frames_per_trans):
            prog = (t + 1) / frames_per_trans
            fr, part = reveal_frame(base, tgt, comps, prog, part)
            out.append(fr)
    for _ in range(20):
        out.append(stages[-1])
    return out

stages = load_stages()
print(str(len(stages)) + ' stages ' + str(stages[0].shape), flush=True)
left = make_left_card()
right_frames = build_right_frames(stages, frames_per_trans=12)
print(str(len(right_frames)) + ' right frames', flush=True)

import tempfile, subprocess, shutil
work = tempfile.mkdtemp(prefix='shiva_v0_')
fdir = os.path.join(work, 'frames')
os.makedirs(fdir, exist_ok=True)
for idx, rf in enumerate(right_frames):
    canvas = np.zeros((H, W, 3), dtype=np.uint8)
    canvas[:, 0:LEFT_W] = left
    canvas[:, LEFT_W:] = (235, 228, 214)
    rh, rw = rf.shape[:2]
    x0 = LEFT_W + (RIGHT_W - rw) // 2
    y0 = (H - rh) // 2
    canvas[y0:y0 + rh, x0:x0 + rw] = rf
    cv2.line(canvas, (LEFT_W, 0), (LEFT_W, H), (180, 160, 130), 2)
    cv2.imwrite(os.path.join(fdir, 'f_%05d.png' % idx), canvas)

fl = os.path.join(work, 'frames.txt')
with open(fl, 'w') as f:
    for k in range(len(right_frames)):
        fp = os.path.join(fdir, 'f_%05d.png' % k)
        f.write('file ' + "'" + fp + "'\n")
        f.write('duration %.4f\n' % (1.0 / FPS))
    fp = os.path.join(fdir, 'f_%05d.png' % (len(right_frames) - 1))
    f.write('file ' + "'" + fp + "'\n")

os.makedirs('/tmp/opencode/shiva_v0', exist_ok=True)
out = '/tmp/opencode/shiva_v0/shiva-s1-1-v0.mp4'
r = subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', fl,
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', str(FPS), out],
                   capture_output=True, text=True)
if r.returncode != 0:
    print('FFMPEG FAIL: ' + r.stderr[-500:])
else:
    print('DONE ' + out + ' ' + str(os.path.getsize(out) // 1024) + 'KB ' +
          str(len(right_frames) / FPS) + 's')
shutil.rmtree(work, ignore_errors=True)
