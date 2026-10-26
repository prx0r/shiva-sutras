"""v1: left = timeline-driven (verse -> quote -> diagram), right = ambient loop."""
import cv2, glob, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, '/root/sleepdraw')
from progressive_journey import diff_mask, component_order, reveal_frame

W, H = 1920, 1080
LEFT_W, RIGHT_W, FPS = 1280, 640, 15

def font(sz):
    try:
        return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', sz)
    except Exception:
        return ImageFont.load_default()

def left_verse():
    img = Image.new('RGB', (LEFT_W, H), (247, 242, 232))
    d = ImageDraw.Draw(img)
    d.text((80, 60), 'SIVA SUTRAS  |  S1-1 / 77  |  00:00-00:06  B1 CHANT', font=font(28), fill=(120, 90, 60))
    d.text((80, 130), 'Caitanyam atma', font=font(96), fill=(25, 25, 25))
    d.text((80, 260), 'Consciousness is the Self.', font=font(54), fill=(60, 60, 60))
    d.text((80, 350), 'Dyczkowski, Aphorisms of Siva', font=font(32), fill=(110, 110, 110))
    d.line([(80, 430), (LEFT_W - 80, 430)], fill=(200, 180, 150), width=2)
    d.text((80, 460), 'PLAIN', font=font(28), fill=(120, 90, 60))
    d.text((80, 500), 'consciousness is the self', font=font(48), fill=(40, 40, 40))
    d.text((80, H - 110), 'LEFT = timeline  |  VERSE CARD', font=font(26), fill=(140, 130, 115))
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def left_quote():
    img = Image.new('RGB', (LEFT_W, H), (247, 242, 232))
    d = ImageDraw.Draw(img)
    d.text((80, 60), 'S1  |  dl1-04  00:17:14  DYCZKOWSKI', font=font(28), fill=(120, 90, 60))
    d.text((80, 130), '"that the self or the ultimate nature', font=font(52), fill=(25, 25, 25))
    d.text((80, 200), 'of all things is Shiva himself,', font=font(52), fill=(25, 25, 25))
    d.text((80, 270), 'who is in reality Chaitanya,', font=font(52), fill=(25, 25, 25))
    d.text((80, 340), 'pure consciousness."', font=font(52), fill=(25, 25, 25))
    d.line([(80, 470), (LEFT_W - 80, 470)], fill=(200, 180, 150), width=2)
    d.text((80, 500), 'CONTEXT: vs man-God difference view', font=font(32), fill=(110, 110, 110))
    d.text((80, 550), 'PAIR: Baumer ss3-10 (cross-voice A/A)', font=font(32), fill=(110, 110, 110))
    d.text((80, H - 110), 'LEFT = timeline  |  QUOTE CARD (verbatim, timestamped)', font=font(26), fill=(140, 130, 115))
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def left_diagram_base(prog=1.0):
    """Four levels of the word: vaikhari -> madhyama -> pasyanti -> para. prog 0..1 reveals."""
    img = Image.new('RGB', (LEFT_W, H), (247, 242, 232))
    d = ImageDraw.Draw(img)
    d.text((80, 60), 'S1  |  ss1-04  DIAGRAM: four levels of the word', font=font(28), fill=(120, 90, 60))
    levels = [('vaikhari', 'spoken out loud'), ('madhyama', 'mental whisper'),
              ('pasyanti', 'visionary seeing'), ('para', 'supreme, undifferentiated')]
    n_show = max(1, int(round(prog * 4)))
    y0 = 200
    for i, (name, gloss) in enumerate(levels):
        y = y0 + i * 170
        active = i < n_show
        col = (25, 25, 25) if active else (190, 180, 165)
        bar = (150, 110, 70) if active else (215, 205, 190)
        d.rectangle([80, y, 110, y + 90], fill=bar)
        d.text((140, y - 10), name, font=font(56), fill=col)
        if active:
            d.text((140, y + 60), gloss, font=font(32), fill=(110, 110, 110))
        if i < 3:
            ac = (150, 110, 70) if i + 1 < n_show else (215, 205, 190)
            d.line([(95, y + 90), (95, y + 170)], fill=ac, width=4)
    d.text((80, H - 110), 'LEFT = timeline  |  DIAGRAM (animated explainer, beat-synced)', font=font(26), fill=(140, 130, 115))
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

# right ambient: 01 stages looped
files = sorted(glob.glob('/root/sleepdraw/storyboards/01-stage-*.png'))
stages = [cv2.imread(f, cv2.IMREAD_COLOR) for f in files]
seq = []
for _ in range(10):
    seq.append(stages[0])
for i in range(1, len(stages)):
    m = diff_mask(stages[i-1], stages[i])
    comps = component_order(m)
    part = np.zeros(m.shape, dtype=bool)
    for t in range(8):
        fr, part = reveal_frame(stages[i-1], stages[i], comps, (t+1)/8, part)
        seq.append(fr)
for _ in range(10):
    seq.append(stages[-1])
print('right ambient frames: ' + str(len(seq)), flush=True)

# timeline: 0-4s verse, 4-8s quote, 8-12s diagram animates
total = 12 * FPS
import tempfile, subprocess, shutil
work = tempfile.mkdtemp(prefix='shivav1_')
fdir = os.path.join(work, 'frames')
os.makedirs(fdir, exist_ok=True)
lv, lq = left_verse(), left_quote()
ri = 0
for k in range(total):
    t = k / FPS
    if t < 4:
        left = lv
    elif t < 8:
        left = lq
    else:
        left = left_diagram_base(prog=min(1.0, (t - 8) / 4))
    rf = seq[ri % len(seq)]
    ri += 1
    canvas = np.zeros((H, W, 3), dtype=np.uint8)
    canvas[:, 0:LEFT_W] = left
    canvas[:, LEFT_W:] = (214, 228, 235)[::-1]  # warm grey (BGR)
    rh, rw = rf.shape[:2]
    x0 = LEFT_W + (RIGHT_W - rw) // 2
    y0 = (H - rh) // 2
    canvas[y0:y0+rh, x0:x0+rw] = rf
    cv2.line(canvas, (LEFT_W, 0), (LEFT_W, H), (180, 160, 130), 2)
    cv2.putText(canvas, 'RIGHT = ambient', (LEFT_W + 20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (130, 120, 105), 2)
    cv2.imwrite(os.path.join(fdir, 'f_%05d.png' % k), canvas)

fl = os.path.join(work, 'frames.txt')
with open(fl, 'w') as f:
    for k in range(total):
        fp = os.path.join(fdir, 'f_%05d.png' % k)
        f.write('file ' + "'" + fp + "'\n")
        f.write('duration %.4f\n' % (1.0 / FPS))
    fp = os.path.join(fdir, 'f_%05d.png' % (total - 1))
    f.write('file ' + "'" + fp + "'\n")
os.makedirs('/tmp/opencode/shiva_v0', exist_ok=True)
out = '/tmp/opencode/shiva_v0/shiva-v1-timeline.mp4'
r = subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', fl,
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', str(FPS), out],
                   capture_output=True, text=True)
print('DONE ' + out + ' ' + str(os.path.getsize(out)//1024) + 'KB' if r.returncode == 0 else 'FAIL ' + r.stderr[-400:])
shutil.rmtree(work, ignore_errors=True)
