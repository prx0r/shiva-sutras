#!/usr/bin/env python3
"""listen.py — machine ears for audio QA. Sends an mp3 and gets back a
flaw-hunt: joints, drag, deictics, pronunciation. Engine piece: works for
any cut or master (essence, heads, full walk later).

Default engine (owner decision 2026-10-26): DashScope Singapore
qwen3.8-omni-flash, thinking off — ~$0.001 per 5-min pass, cheapest
working option (retired omni-turbo line replaced; OpenRouter gpt-audio-mini
kept as fallback, ~$0.003/pass).

Usage: python3 tools/listen.py <mp3> [prompt-name] [--fallback]
Prompts: qa, joints, deictics, verify, critic (ratings + advice + verdict), cast (voice-casting for TTS seats).
"""
import re, json, urllib.request, urllib.error, base64, sys, os

QWEN_URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions"
QWEN_MODEL = "qwen3.8-omni-flash"

PROMPTS = {
"qa": "You are the QA ears for a spoken-word audio piece (bell, spoken section intros, human Sanskrit chant, synthetic English narration, human lecture clips, pauses). Listen to the whole file.\n1. TRANSCRIPT SKETCH: one line per voice segment (voice: first 8 words).\n2. NEW VOICE CHECK: is the synthetic narrator human-sounding and consistent? Any misreads?\n3. NEW FLAWS, located by quoting neighboring content (NOT timecodes): cut-off words, room jumps, draggy stretches, dead/rushed pauses, anything confusing.\n4. JOINTS: each voice-to-voice handover, CLEAN or RUBBED with quoted location.\n5. DEICTICS: any 'they/it/this' whose referent is unclear — quote it, say what you think it means.\n6. VERDICT: FLOW / NO-FLOW.",
"joints": "List every voice-to-voice handover with quoted neighboring content (NOT timecodes). Voices: bell/sine, synthetic narration (TTS), human chant (Sanskrit), human lecture (English). Each: quoted location, from-voice → to-voice, CLEAN or RUBBED in ≤12 words.",
"deictics": "Transcribe the first sentence of every human lecture clip with its quoted location. For each, list every pronoun (they/them/it/this/that) and state its referent from context, or flag it as unbound.",
"audit": "Return ONLY valid JSON (no prose): {\"verdict\": \"FLOW\" or \"NO-FLOW\", \"ratings\": [{\"cue\": <section name>, \"flow\": 1-5, \"why\": \"<12 words quoted>\"}], \"flaws\": [{\"where\": \"<quoted neighbors>\", \"what\": \"<12 words>\", \"fix\": \"<12 words>\"}], \"pronunciation\": [{\"word\": w, \"heard\": h}], \"advice\": \"<one sentence>\"}. Judge a spoken-word piece: bell, spoken intros, human Sanskrit chant, synthetic English narration, human lecture clips, pauses. Flag mid-word cuts, room jumps, draggy stretches, dead/rushed pauses, unclear pronouns (quote them), misread words.",
"verify": "Targeted re-check only (fixes were applied since your last pass): 1. Is the synthetic narrator human-sounding, no misreads? Quote any misread word. 2. Any remaining cut-off words, room jumps, draggy stretches, dead pauses — quote locations. 3. VERDICT: FLOW / NO-FLOW with blocking quotes.",
"chantcheck": "Transcript sketch first (one line per voice segment: voice + first 8 words). Then flag EVERY moment where a speaker announces they are about to chant, recite, read, sing, or say a verse/text AND the announced thing does not happen within 15 seconds — quote the announcement and describe what actually follows. Also flag any chant/recitation appearing WITHOUT introduction at an odd place (e.g. stranded at the very end). End with NONE if clean.",
"surgery": "This is ONE isolated clip; judge ONLY its two edges and voice. Report exactly: 1. FIRST3: the first 3 words you hear. 2. LAST3: the last 3 words you hear. 3. HEAD: CLEAN onset / MID-WORD cut / dead air before speech (rough ms). 4. TAIL: COMPLETE sentence / MID-WORD cut / MID-SENTENCE strand / abrupt digital cutoff vs natural decay. 5. VOICE: one line — speaker type, room (dry/close vs hall/reverb), delivery note. 6. VERDICT: CLEAN or CUT (if CUT: extend head by X words/ms and/or tail by X words/ms — be exact). Only what you HEAR; never infer beyond the clip.",
"critic": "You are the critic. Listen to the whole piece (bells, spoken intros, human Sanskrit chant, synthetic English narration, human lecture clips, pauses). Return EXACTLY: A. Per-section ratings — for the opening, each question-answer cell, each section head: FLOW 1-5 plus one quoted reason. B. TOP 3 FLAWS — quoted location, what is wrong, suggested fix. C. ADVICE — one paragraph: the single change that improves this most. D. VERDICT: FLOW / NO-FLOW with blocking quotes.",
"cast": "This is ONE isolated TTS sample for voice-casting (single Sanskrit verse, one synthetic voice). Judge ONLY what you hear: 1. HEARD: transcribe it in plain roman letters exactly as spoken. 2. CLARITY 1-5: are the Sanskrit sounds distinct (separate syllables, clean consonants, even pace) or slurred/mumbled/absent? Quote the clearest and the muddiest word. 3. CHARACTER: one line — impression of age/gender and steadiness (noisy/theatrical vs plain). 4. VERDICT: CAST or PASS with the quoted reason. Never infer beyond the clip.",
}

def _env(key):
    for f in [os.path.expanduser("~/.config/opencode/.env")]:
        try:
            m = re.search(rf"^{key}=(.*)$", open(f).read(), re.M)
            if m and m.group(1).strip():
                return m.group(1).strip()
        except OSError:
            pass
    return None

def _qwen(mp3, prompt):
    key = _env("DASHSCOPE_API_KEY")
    aud = base64.b64encode(open(mp3, "rb").read()).decode()
    body = json.dumps({"model": QWEN_MODEL,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "input_audio", "input_audio": {"data": f"data:audio/mp3;base64,{aud}", "format": "mp3"}},
        ]}],
        "reasoning_effort": "none",
        "max_tokens": 1500}).encode()
    req = urllib.request.Request(QWEN_URL, data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    out = json.load(urllib.request.urlopen(req, timeout=600))
    return out["choices"][0]["message"]["content"], out.get("usage")

def _openrouter(mp3, prompt):
    key = _env("OPENROUTER_API_KEY")
    aud = base64.b64encode(open(mp3, "rb").read()).decode()
    body = json.dumps({"model": "openai/gpt-audio-mini", "modalities": ["text"],
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "input_audio", "input_audio": {"data": aud, "format": "mp3"}},
        ]}]}).encode()
    req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                 "HTTP-Referer": "https://github.com/prx0r/shiva-sutras", "X-Title": "shiva-sutras-qa"})
    out = json.load(urllib.request.urlopen(req, timeout=600))
    return out["choices"][0]["message"]["content"], out.get("usage")

def main():
    mp3 = sys.argv[1]
    pname = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else "qa"
    fallback = "--fallback" in sys.argv
    try:
        text, usage = _qwen(mp3, PROMPTS[pname])
        engine = "qwen3.8-omni-flash"
    except Exception as e:
        if not fallback:
            raise
        text, usage = _openrouter(mp3, PROMPTS[pname])
        engine = "gpt-audio-mini-fallback"
    print(text)
    print(f"\n[engine: {engine} | usage: {usage}]")

if __name__ == "__main__":
    main()
