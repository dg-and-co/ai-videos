# WINKKO drill ad v1 — "Weightless"

12 s · 9:16 (1080×1920, master at 4K if upscaled) · 24 fps · no voice-over · music + SFX only

## Brief

Dark, dim studio. One product: the WINKKO HD Professional 20V brushless drill with the
2.0Ah ION battery. The drill floats. The battery floats under it. Detail shots. Dramatic,
smooth, premium. Ends on a white end card with a red border (#e40213), the logo, the slogan
"Alvöru verkfæri, rétt verð", and the address "Smiðjuvegur 36 – Rauð gata" where
"Rauð gata" turns red.

## What the reference does, and what we do better

| Reference (10 s)                                   | Ours (12 s)                                                    |
| -------------------------------------------------- | -------------------------------------------------------------- |
| Macro on torque ring, then grip, then a hand grabs | No hands. The tool is alone and weightless the whole way       |
| Flat grey studio, one soft key                     | Same darkness, but a red rim light and drifting dust for depth |
| Battery floats below drill for ~1 s               | The battery/drill separation is a full beat, then it locks in  |
| Plain white end card, letters scatter into place   | Red border draws on, logo settles, "Rauð gata" turns red       |
| Battery text is AI-garbled                         | Keyframes are locked from the real product photos first        |

## Look

- **Set**: near-black concrete floor and backdrop, soft overhead spot with a tight pool of
  light (matches the hero photos). Faint haze so the light has volume. Slow-drifting dust.
- **Accent**: a thin red rim light (brand red) that catches the trigger, the battery latch
  and the chuck ring edge. Never colours the whole frame.
- **Camera**: slow, heavy, gimbal-smooth. Long lens for macros, mild wide for the hero.
  Every move is slow-then-snap: ease in, hold, then a quick finish into the cut.
- **Product truth**: chuck, silver torque collar (numbers 16–20), red trigger, textured grip,
  "20V" badge on the grip, WINKKO HD Professional badge on the motor housing, red battery
  latch, LED fuel gauge, work light above the battery foot.

## Shot list

| #   | Time        | Shot                  | Framing and move                                                                                                                                                                                         | Sound                                                     |
| --- | ----------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 1   | 0.0 – 2.0   | Ignition (macro)      | Black. A light sweeps left-to-right across the knurled chuck and silver torque collar, revealing "16 · 18 · 20". The chuck turns a slow quarter rotation. Extreme close-up, shallow focus, red rim on the collar edge. | Sub-bass hum fades up. One soft metallic click as the ring passes. |
| 2   | 2.0 – 4.5   | Levitation (hero)     | Cut to a 3/4 front hero, mid-frame. The drill hangs in the air, slowly rotating ~30°. The 2.0Ah battery hovers 10 cm below it, aligned to the foot, drifting in the same rhythm. Dust motes in the beam. Slow push-in. | Airy whoosh on the cut. Low pulse begins, like a heartbeat. |
| 3   | 4.5 – 6.5   | Lock-in (low angle)   | Low angle from behind the battery, looking up. The battery rises and snaps into the drill's foot. On the click the LED fuel gauge lights 4 bars and the work light flashes on, throwing a hard pool of light onto the floor. | Solid mechanical click, then an electric charge-up rise.  |
| 4   | 6.5 – 8.5   | Profile orbit         | Side profile (matches the side photo). Camera orbits ~60° around the floating tool at eye level. Red rim slides along the trigger and the WINKKO badge passes through the key light. Speed ramps from slow to fast in the last half second. | Riser builds under the orbit.                             |
| 5   | 8.5 – 9.5   | Impact                | The drill snaps to a camera-facing hero pose with a flash of light. The chuck spins for half a second (motion blur). Hard cut on the beat to white.                                                      | Short motor rev, then an impact hit that lands on the cut. |
| 6   | 9.5 – 12.0  | End card              | White. A red border (#e40213, ~40 px inset) draws itself around the frame in 0.6 s. The WINKKO HD Professional logo settles in from 92% to 100% scale with a soft fade. Slogan fades in under it: "ALVÖRU VERKFÆRI, RÉTT VERÐ". Then "Smiðjuvegur 36 – Rauð gata" fades in in black, and at ~10.8 s "Rauð gata" turns red (#e40213) with a small scale pulse. Hold to 12.0. | Whoosh into near-silence. A single soft tick when "Rauð gata" turns red. Music tail rings out. |

Total: 12.0 s. Footage 9.5 s, end card 2.5 s.

## Music and SFX

- No voice-over.
- Higgsfield has no standalone music or SFX model. The video models generate diegetic audio
  with each clip (sound on), which gives usable clicks, whooshes, motor and hum. We keep the
  best of that as the SFX bed.
- Music: a licensed track from you (dark, slow, cinematic, ~90–100 BPM so beats land on the
  cuts at 2.0 / 4.5 / 6.5 / 8.5 / 9.5 s), or we go SFX-only with a low drone. Decision needed.

## Production plan

1. **Keyframes (stills, ~2 credits each).** Generate a 9:16 still per shot from the product
   photos as references, so composition, lighting and product details are locked before any
   video credits are spent. 5 shots × 2 candidates ≈ 20 credits. You approve one frame per shot.
2. **Motion (image-to-video).** Kling 3.0 pro, 9:16, 5 s per shot, start frame = approved
   keyframe, end frame where the move needs a precise finish (shots 3 and 5). 10 credits per
   clip, 2 candidates per shot ≈ 100 credits. Cinema Studio v2 (18 credits, up to 12 s,
   multi-shot) is the fallback if a single continuous take reads better.
3. **End card.** Rendered locally, not generated: HTML/CSS animation captured frame-by-frame
   with Chromium at 1080×1920, so the hex colour, the type and the timing are exact.
4. **Assembly.** ffmpeg: trims and speed ramps to the timeline above, cuts on beats, music
   and SFX mix, loudness normalised, 1080×1920 H.264 master. Optional 4K upscale via
   Higgsfield `upscale_video` on the final cut.

Budget for v1 including candidates: roughly 130–200 credits of the 1,200 available.

## Assets

See `media.json` for Higgsfield media IDs. Local files live under `assets/`.
