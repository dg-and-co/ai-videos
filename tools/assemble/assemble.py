#!/usr/bin/env python3
"""Assemble the WINKKO drill ad v1: five Seedance clips + rendered end card + synthesized SFX bed.

Usage: python3 assemble.py <clips_dir> <endcard_mp4> <out_mp4> [--edl edl.json]
Each shot in the EDL: {"file": "shot1.mp4", "in": 0.5, "dur": 1.5, "speed": 1.6, "fade_white": 0.0}
'dur' is the OUTPUT duration; source span = dur * speed starting at 'in'.
"""
import json, os, subprocess, sys, shlex
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
FPS, W, H = 24, 1080, 1920

DEFAULT_EDL = [
  {"file": "shot1.mp4", "in": 0.4, "dur": 1.5, "speed": 1.6},
  {"file": "shot2.mp4", "in": 0.2, "dur": 2.5, "speed": 1.4},
  {"file": "shot3.mp4", "in": 0.0, "dur": 2.0, "speed": 2.0},
  {"file": "shot4.mp4", "in": 0.6, "dur": 1.5, "speed": 1.8},
  {"file": "shot5.mp4", "in": 0.0, "dur": 2.0, "speed": 2.0, "fade_white": 0.15},
]
ENDCARD_DUR = 2.5

def atempo_chain(speed):
    # ffmpeg atempo accepts 0.5..2.0 per stage (newer builds 0.5..100, but chain to be safe)
    parts = []
    s = speed
    while s > 2.0:
        parts.append("atempo=2.0"); s /= 2.0
    while s < 0.5:
        parts.append("atempo=0.5"); s /= 0.5
    parts.append(f"atempo={s:.4f}")
    return ",".join(parts)

def main():
    clips_dir, endcard, out = sys.argv[1], sys.argv[2], sys.argv[3]
    edl = DEFAULT_EDL
    if "--edl" in sys.argv:
        edl = json.load(open(sys.argv[sys.argv.index("--edl") + 1]))
    inputs, vf, af = [], [], []
    for i, s in enumerate(edl):
        inputs += ["-i", os.path.join(clips_dir, s["file"])]
        span = s["dur"] * s["speed"]
        fw = s.get("fade_white", 0.0)
        fade = f",fade=t=out:st={s['dur']-fw:.3f}:d={fw:.3f}:color=white" if fw > 0 else ""
        vf.append(f"[{i}:v]trim=start={s['in']}:end={s['in']+span:.3f},setpts=(PTS-STARTPTS)/{s['speed']},"
                  f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},format=yuv420p{fade}[v{i}]")
        af.append(f"[{i}:a]atrim=start={s['in']}:end={s['in']+span:.3f},asetpts=PTS-STARTPTS,{atempo_chain(s['speed'])},"
                  f"aresample=48000,afade=t=in:d=0.05,afade=t=out:st={s['dur']-0.08:.3f}:d=0.08[a{i}]")
    n = len(edl)
    inputs += ["-i", endcard]
    vf.append(f"[{n}:v]scale={W}:{H},fps={FPS},format=yuv420p[v{n}]")
    footage = sum(s["dur"] for s in edl)
    total = footage + ENDCARD_DUR
    # Synthesized bed: low drone (55+110 Hz with slow tremolo) + filtered noise, swelling to the cut, then a sub hit at the cut and a tick when "Rauð gata" turns red.
    t_hit, t_tick = footage, footage + 1.30
    bed = (f"sine=frequency=55:sample_rate=48000:duration={total},volume=0.9[s1];"
           f"sine=frequency=110:sample_rate=48000:duration={total},volume=0.35[s2];"
           f"anoisesrc=color=brown:sample_rate=48000:duration={total}:amplitude=0.6,lowpass=f=400[nz];"
           f"[s1][s2][nz]amix=inputs=3:normalize=0,"
           f"volume='if(lt(t,{footage}),0.25+0.55*t/{footage},0.06)':eval=frame,"
           f"tremolo=f=0.4:d=0.35,afade=t=in:d=1.2,alimiter=limit=0.9[bed];"
           f"sine=frequency=45:sample_rate=48000:duration=1.4,volume='exp(-3.5*t)':eval=frame,adelay={int(t_hit*1000)}|{int(t_hit*1000)},apad=whole_dur={total}[hit];"
           f"sine=frequency=2400:sample_rate=48000:duration=0.03,volume=0.35,afade=t=out:d=0.02,adelay={int(t_tick*1000)}|{int(t_tick*1000)},apad=whole_dur={total}[tick]")
    concat_v = "".join(f"[v{i}]" for i in range(n + 1)) + f"concat=n={n+1}:v=1:a=0[vout]"
    concat_a = "".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1,apad=whole_dur={total}[sfx]"
    mix = "[sfx][bed][hit][tick]amix=inputs=4:normalize=0:weights=1 0.8 1 1,loudnorm=I=-14:TP=-1.5:LRA=9,aformat=sample_rates=48000:channel_layouts=stereo[aout]"
    graph = ";".join(vf + af + [concat_v, concat_a, bed, mix])
    cmd = [FF, "-hide_banner", "-loglevel", "error", "-y", *inputs, "-filter_complex", graph,
           "-map", "[vout]", "-map", "[aout]", "-t", f"{total:.3f}", "-r", str(FPS),
           "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-movflags", "+faststart", out]
    print("total", total, "s; footage", footage, "s")
    subprocess.run(cmd, check=True)
    print("wrote", out)

if __name__ == "__main__":
    main()
