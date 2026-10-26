# VISUAL ENGINE SPEC v1 — left teaches, right holds (1920×1080)

Status: prototype v0/v1 rendered 2026-10-26 (`tools/visual_prototype_v0.py`,
`tools/visual_prototype_v1.py`). Outputs (not committed): R2
`stallshark/journey/shiva-s1-1-v0.mp4` (11s static) +
`stallshark/journey/shiva-v1-timeline.mp4` (12s switching left).

## 1. Layout (locked)
* Canvas 1920×1080, 15fps, H.264 yuv420p. Divider 2px at x=1280 (#B4A082).
* Left 1280×1080 warm paper #F7F2E8, 80px margins. Right 640×1080, art
  620×900 centered (x=1290, y=90). Right frames come from
  `sleepdraw/progressive_journey.py` (light paper, continuous, no fades).
* Fonts: serif; Sanskrit diacritics verified vs print before lock
  (MISTAKES M8 rule).

## 2. LEFT — timeline-driven (what is being said)
Source: `build/manifest_s{1..6}_{A,B,C}.json` beats
(uid, t_in, t_out, dur, title) + `build/TRACK_F_STORYBOARD.md` (77 verses)
+ `build/BEATS.md` grammar. Four templates only:

| Template | When | Content |
|---|---|---|
| QUESTION | Section opener | Manifest `question`, large. 2-breath hold. |
| VERSE | B1 chant → B2 readout | Sanskrit + translation + plain + ref (manifest `card` + TRACK_F row). |
| QUOTE | B3/B4 archive clip | Verbatim `quote` from `excavations/{ss,dl}.md` + uid + timestamp + one-line context + pair. Never paraphrase. |
| DIAGRAM | Beat title needs it | Animated explainer, 0→1 progress over beat. Registry below; fallback = QUOTE. |

Switch on beat boundaries. Max 4-frame dissolve, nothing fancier.

## 3. RIGHT — ambient beauty (free-running, never synced)
Source: `sleepdraw/storyboards/journey-pairs.json` — 72 Shiva-family hits
(Mahakala, Kali, Ganesha) + 3 owner 12-stage prototypes (620×900).
Renderer: `sleepdraw/progressive_journey.py`.
Rules: one deity at a time → hold final ~1.5s → 12-frame crossfade → next.
Never black, never blank-reset, never text. Independent clock — left cuts
never restart or pause right. Playlist: `playlists/deity-cast.json`
(default: owner-01 → Mahakala ×3 → Kali → Ganesha → owner-02 → repeat).

## 4. Diagram registry (new art only with a source span)
* `four-levels-word` (ss1-04): vaikhari → madhyama → paśyanti → para ladder
  (v1 built in `visual_prototype_v1.py:left_diagram_base`).
* `three-states-turya` (S4): waking/dreaming/deep-sleep → turya ring.
* `tattva-ladder` (36): Siva → earth, collapsible to 3 clusters.
* `screen-canvas` (ss5-01 jagat-citra): figures on an unchanging screen.
* `rock-terma` (revelation): boulder → text underneath.
No diagram ships without the Bäumer/Dyczkowski line that describes it.

## 5. Audio (exists — do not rebuild)
`tools/make_audio.py` + `build/BEATS.md`: bells 880/220Hz, TTS
questions/Sanskrit/translation/plain, archive cuts per manifest,
loudnorm I=-16. Left cuts align to the same t_in/t_out audio uses.

## 6. Build
```
python3 tools/visual_left.py --manifest build/manifest_s1_A.json --out /tmp/left/
python3 tools/visual_right.py --playlist playlists/deity-cast.json --out /tmp/right.mp4
ffmpeg -i /tmp/left/%05d.png -i /tmp/right.mp4 -i audio/LA.wav \
  -filter_complex "..." -c:v libx264 -c:a aac out/s1A.mp4
```
Stream frames (disk 96%). Finals → R2 `stallshark/journey/`. Prototypes
v0 (static card) / v1 (verse→quote→diagram + ambient right) are the
reference implementations to promote into `tools/visual_left.py` /
`tools/visual_right.py` at template lock.

## 7. QA gates
* `process/verify.sh` green (units 307/0, G0 7/7, plain MATCH) after any edit.
* Every left string grep-able to `text/`, `excavations/`, or §4 registry.
* Right: no freeze >3s, no black, no text. Sanskrit checked vs print.
* Owner ear on audio first; video never reorders audio.

## 8. Open
1. S1 beat→template map (~15 diagrams?) — draft from beat titles, owner veto.
2. Deity cast: Mahakala-heavy vs Bhairava-first (new checkpoints via
   wan2.7-image + sleepdraw `axioms.py`).
3. Serif + diacritics lock.
