# Handoff Spec: Kalam promo motion graphics

A complete record of the Kalam (كلام) promo-video work in this chat: what was asked for, what you supplied, the scripts and shots, every correction, the design and motion specs, and how each final video was built and delivered.

The focus is the motion graphics. Generating and editing the film stills (the Magnific image work) is out of scope. The film intro appears only as the post-production and motion work that was done on those finished stills.

---

## 1. Overview

**Product:** Kalam, a private voice-to-text app for Mac. You hold Right Option ⌥, speak, and let go, and your words are typed wherever the cursor is. It handles Arabic and English, including Gulf and Omani Arabic, Modern Standard Arabic, Egyptian and Levantine. It runs on the Mac, with no account, no subscription and no cloud.

**Source of truth for facts:** `KALAM.md`. The standing rule from the first brief was not to invent features that aren't in `KALAM.md`.

**Taglines:** English *Write less, speak more.* and Arabic *اشرح بلا حدود*. They are kept as a pair, since the Arabic is not a direct translation.

**Who it's for:** social video (Reels, TikTok, Shorts) and the website. Every cut after the first one is vertical.

### Final deliverables

| File | What | Format | Length | Status |
|---|---|---|---|---|
| `kalam-promo.mp4` | First promo, landscape | 1920×1080 | 44 s | Superseded |
| `kalam-promo-vertical.mp4` | Vertical cut ("Sara", then the "Halima" parallax version) | 1080×1920 | 42 s | Superseded, used as motion reference |
| `kalam-promo-vertical-calm.mp4` | Calm 3D cut on your assets | 1080×1920 | 60 s | Draft |
| `kalam-promo-vertical-lively.mp4` | Lively 3D-swing cut | 1080×1920 | 60 s | Draft |
| **`kalam-promo-vertical-dynamic.mp4`** | Dynamic parallax cut on your backgrounds | 1080×1920 | 60 s | **Final, top quality** |
| **`kalam-promo-ar.mp4`** | Arabic-only 10-section promo | 1080×1920 | 66 s | **Final, top quality** |
| **`kalam-install.mp4`** | How to install Kalam, 8 steps | 1080×1920 | 76 s | **Final, top quality** |
| **`kalam-film.mp4`** | Film-style intro on the silhouette stills | 1080×1920 | 49 s | **Final, top quality** |
| `FILM-SCRIPT.md` | Scene script for the film, with no on-screen text and the multi-person ending as an optional suggestion | Markdown | n/a | Delivered |

The finals are on the `promo-videos` branch (see §9).

---

## 2. What you supplied

| Input | Used for |
|---|---|
| `KALAM.md` (in the repo) | All feature claims and wording |
| 9 app screenshots: Home EN and AR, Notes, Clipboard, Your words, Shortcuts, Settings, Settings › Sound | Real app screens in every cut, cropped to `assets/screens/*.png` |
| Brand assets: `logo-full.svg` wordmark, Kalam app icon, megaphone banner (EN and AR) | End cards, icon pops |
| 5 nav icons (SVG): Home, Notes, Clipboard, Your words, Shortcuts | Bilingual-app scene (icons light up as each screen appears) |
| `Asset_6.svg` plus a palette sheet | Palette reference (`assets/ui/palette-reference.png`) |
| Recording bar reference: first a white pill with coral bars, later the **original app bar** screenshot (dark frosted capsule, 11 bars orange → yellow → blue) | Recording bar. The original one is used everywhere from the Arabic cut on. |
| Backgrounds, 1080×1920: banner blue, cream, sky, blue glow, person writing, hands glow, orange, orange glow, clouds, person with beam, diagonal, diagonal soft, pastel, sky peach, blue bars, blue clear, blue cream, sky soft | Per-scene backgrounds (`assets/bg/`) |
| Voice-orb image | Calm cut. It was removed from the opening and reused blurred in the background. |
| Reference videos: the "Sara" and "Halima" vertical cuts (sent back as references twice) | Motion reference for the dynamic cut and Arabic section 8 |
| Edited `SCRIPT.md` | Vertical cut copy and story |
| 21-artboard storyboard screenshot plus per-section background images | Arabic 10-section cut |
| Burst animation reference screenshot (motion only, not its colours) | Burst on cards, bubbles, pills, chips and screens |
| Circle-reveal transition reference | Arabic section 1 → 2 transition |
| Arabic copy for the 10 sections | Arabic cut captions |
| `480.mov`, a 640×404 screen recording of the install | Install reel (wording copied; windows rebuilt as crisp mockups) |
| `KALAM_VIDEO_PROJECT_SUMMARY.md` (film brief) plus 10 approved stills | Film intro (`promo/FILM-BRIEF.md`, `assets/film/`) |

---

## 3. Design tokens

### Colour (your palette sheet values, chosen over the app CSS so everything matches your icons)

| Token | Value | Usage |
|---|---|---|
| `color-coral` | `#EE7A4A` | Primary accent: key glow, icon glow, caret, rings, strike line, dialect tags |
| `color-amber` | `#EDB04C` | Glow falloff, burst dots |
| `color-sky` | `#5B9BD6` | Burst dots, "You say" dot |
| `color-navy` | `#2D5A96` | Deep-blue scenes |
| `color-teal` | `#2E8393` | ✓ check circles, active Shortcuts icon |
| `color-ink` | `#14212E` | All dark text, key chips, wordmark on light backgrounds |
| `color-muted` | `#5E6E78` | Card meta labels |
| `color-cream` | `#F7F0EB` | Stage background |
| `color-blush` | `#F6DDD3` | Film gradient bottom |
| `color-mist` | `#C9D7E6` | Film gradient top |
| `color-night` | `#0F1D33` | Night tint (privacy, calm cut) |
| `rec-stops` | `rgb(253,110,56)` → `rgb(255,194,84)` → `rgb(92,161,209)` | The original recording bar's 11 bars |

### Typography

| Token | Value | Usage |
|---|---|---|
| `font-brand` | Readex Pro, variable 160–700, Arabic plus Latin subsets (local woff2) | All captions, both languages |
| `font-mac` | Inter | macOS mockups (windows, dialogs, menus) |
| `caption-en` (film) | 66 px / 500 / −0.015em / 1.22 | English caption |
| `caption-ar` (film) | 58 px / 500 / 1.5, RTL | Arabic caption, same colour and weight as English |
| `caption-ar` (Arabic cut) | 76 px / 700 (second line 60 px / 600) | Arabic-only captions |
| `card-text` | 40 px / 1.42 | Frosted card body |
| `kbd-chip` | 36 px / 600, white on ink, 16 px radius | Right ⌥ chip |

**Rule you set:** Arabic always uses the same colour and weight as the English. No second font is used to tell the languages apart.

### Surfaces

| Token | Value | Usage |
|---|---|---|
| `glass-frosted` | `rgba(255,255,255,.5)` with `backdrop-filter: blur(26px) saturate(1.3)`, 1.5 px inner white border, radius 34 | Film cards |
| `glass-chip` | Translucent white, thin light border, white text | Arabic section 4 toggle and dialect chips |
| `rec-capsule` | 300×90, radius 45, `rgba(52,44,40,.62)` with blur 18 | Original recording bar |
| `pill-result` | Fully rounded white, teal check circle, slight soft shadow | ✓ result pills |
| `grain` | Film grain over every frame (overlay, opacity about 0.16 in the film; multiply about 0.05 in the promos) | Ties the UI to the photographic backgrounds |

---

## 4. Components

| Component | Variant | Behaviour | Notes |
|---|---|---|---|
| Recording bar | Original app capsule | Bars follow a synthetic speech envelope. While transcribing, they shimmer as a travelling sine. Springs in and fades out. | Replaced the white pill everywhere, at your request |
| Caption | Bilingual (EN over AR) or Arabic-only | Word-by-word entrance | Same colour and weight for both languages. Black on light backgrounds, white on dark blues. |
| Key | Big white "RIGHT ⌥ option" key | Glides in, presses down, white rings pulse out | Arabic cut: stays white, while the small caption chip is black with white text |
| Email or app card | Email, WhatsApp, X, Notes | Lands with a burst | WhatsApp redrawn as the real mark. X replaced Slack (your choice). |
| Chat bubble | Flat coral with a pointed tail, no shadow | Burst on land | Arabic section 4 |
| Language toggle | Glass "English · العربية" | Slides between the two | |
| Dialect chips | Glass: خليجي، عُماني، فصحى، مصري، شامي | Turn in | All the same glass style, with no coral highlight |
| Result pill | ✓ rounded with a soft shadow | Springs or flips up, sometimes with a burst | |
| Burst | 20 dots in brand colours | Fly out over 0.8 s with ease-out, fade and drop slightly | Motion copied from your reference, not its colours |
| Magnifier lens | Round lens with a soft ring | Enlarges a UI target | Arabic section 6, install reel |
| Cursor and ripple | macOS cursor with a coral click ripple | Moves along keyframed paths and holds before each click | Install reel |
| Spotlight | Darkens around the target | With a camera zoom | Install reel |
| Frosted card | Draft, "You say", result, correction, dialect | Rises, un-blurs and fades | Film |
| Kalam icon pop | 210 px icon, coral radial glow, two rings | Spring pop, then flies into the laptop screen | Film shot 3 |
| Screen composite | Virtual 1440×900 Mac screen | Perspective-mapped to the laptop, with a hand matte | Film. Hands stay in front of the UI. |

---

## 5. Motion spec

| Element | Trigger | Animation | Duration | Easing |
|---|---|---|---|---|
| Soft spring (all pop-ins) | On cue | 0 → 1 with about 1% overshoot (ω = 11, ζ = 0.82) | About 0.5 s to settle | Damped spring |
| Caption words (promos) | Scene start, +0.08 s per word, +0.25 s per line | Rise 46 px and scale 0.86 → 1 | Spring | Spring |
| Caption words (film) | +0.075 s per word, +0.32 s for the Arabic line | Rise 26 px, blur 8 px → 0, fade | 0.6 s | Cubic out |
| Caption exit | 0.3–0.35 s before scene end | Fade and lift 24–40 px | 0.3 s | Cubic in-out |
| Parallax scene change (dynamic, Arabic) | Scene boundary | Content slides, background moves at 0.35× and the new scene is revealed with a clip-path; direction alternates | About 0.6 s | Cubic in-out |
| Crossfade (calm) | Scene boundary | Fade with a slight 3D tilt-settle | About 0.6 s | Cubic in-out |
| 3D swing (lively) | Scene boundary | The old scene turns away into depth, the new one swings in from the opposite side, alternating axis | About 0.7 s | Cubic in-out |
| Circle reveal (Arabic 1 → 2) | Key press | The section 2 look grows as a circle from the key, with white rings | About 0.6 s | Cubic out |
| Burst | Card or pill lands | 20 dots out to 200–370 px | 0.8 s | Cubic out |
| Camera zoom (install, Arabic section 6) | Before a small target | Zoom container eased to the focus point, with the lens appearing | 0.6–0.9 s | Cubic in-out |
| Film dolly in | Shots 1 and 6 | Scale 1.00 → 1.07 about the laptop | Whole shot | Cubic in-out |
| Film dolly back | Shot 8 | Scale 1.10 → 1.01 | Whole shot | Cubic in-out |
| Film handheld | Locked shots | Sine drift of ±2–3 px, ±0.08° | Continuous | n/a |
| Film icon fly-in | 2.0 s after the pop | Icon moves and scales to the screen centre, glow fades | 0.55 s | Cubic in-out |
| End card | Last 6–7 s | Icon spring, then wordmark, EN tagline, AR tagline about 0.4–0.5 s apart, rising and un-blurring | 0.7 s each | Cubic out |

**Motion rules that came from your corrections:**
- Less bounce. Only a soft spring with no visible wobble.
- No beat pulse on backgrounds or captions.
- No screen shake, except a small one at the key slam in the dynamic cut.
- Keep the motion elegant and subtle in the calm style, and dynamic but readable in the dynamic style.

---

## 6. Version history: requests, scripts and corrections

### 6.1 First promo, 16:9, 44 s (`scenes.html`)

**Your brief:**
- Hook: typing slowly, then Right ⌥, then the recording bar.
- Any app.
- Arabic and English with dialects.
- Smart touches: scratch that, shortcuts, no fillers.
- Bilingual app: the EN home screen, then the AR one.
- Privacy.
- End card with the logo, both taglines and "Powered by Amira Hamood".
- Look: app palette, megaphone, friendly; bilingual RTL text; upbeat music with no voiceover; Gulf-friendly Arabic.
- Output to `brag-output/`, with `brag-output*/` added to `.gitignore`.
- Wait for approval before generating.

**Scenes:**

| # | Time | Content |
|---|---|---|
| 1 | 0–8 s | Hook: "Hi Sara," with a typo, the Right ⌥ press, the beat drops, the recording bar, the sentence types itself |
| 2 | 8–14 s | Email, WhatsApp (Arabic), Slack, Notes |
| 3 | 14–20 s | Gulf Arabic message, then English, the العربية/English flip, dialect chips |
| 4 | 20–28 s | Meet at 3 → 4, "sign off" shortcut, fillers struck out |
| 5 | 28–34 s | EN home screen with screens fanned behind, then an RTL wipe to the AR home screen |
| 6 | 34–38.5 s | Mac and lock, three privacy chips |
| 7 | 38.5–44 s | Megaphone EN → AR, icon, wordmark, taglines, "Powered by Amira Hamood" |

**Delivered:** in chat (mp4 and poster).

### 6.2 Vertical cut, 1080×1920, 42 s ("Sara", `scenes-vertical.html`)

**Asked:** the same video at 1080×1920, more dynamic and lively.

**Built:**
- Word-by-word pop-in captions.
- A colour per scene.
- Blurred swipe cuts.
- A key "drop" with a shake, a coral fill and rings.
- Beat-synced cards and chips.
- 3D flip from the EN to the AR home screen.
- A punchier track.
- Safe zones kept clear for the Reels and TikTok UI.

### 6.3 Editable script, then the "Halima" parallax cut

**Asked:** send the script so you could edit it (`promo/SCRIPT.md`). You sent back an edited script.

**Your corrections:**
- Vertical only.
- Less bounce overall.
- Keep the dynamic feel, but use a parallax effect.

**Script edits applied:**
- The email goes to **Halima**, with the typo "Hi Halu" fixed to "Hi Halima,".
- WhatsApp: «واصل بعد 10 دقايق، تجهّزي».
- Chat: «شحالش؟ نتلاقى الساعة 4 في الكوفي؟».
- 4a caption: "Changed your mind mid speaking?" / «غيّرت رأيك وانت تتكلم؟».
- "Powered by Amira Hamood" removed from the end card.

**Built:**
- Four depth layers: background, far shapes, content, near shapes.
- Parallax slides between scenes.
- Slow drift within each scene.
- Toned-down pops.

### 6.4 Calm cut, 42 s then 60 s (`scenes-calm.html`)

**Asked:**
- Same vibe as the first video: minimal and clean.
- Subtle 3D, fade in, fade out, elegant.
- Use the visuals, backgrounds and buttons you supplied.
- Vertical.
- Same look-and-feel brief.
- Wait for all files and approval.

**Scene backgrounds:**

| Scene | Background |
|---|---|
| Still typing | Person writing |
| Right ⌥ | Voice orb |
| Any app | Sky |
| Arabic + English | Banner blue |
| Smart touches | Cream |
| Bilingual app | Soft sky (nav icons light up) |
| Privacy | Blue glow under a night tint |
| End card | Megaphone |

**Corrections:**
- Remove the orb from the opening and keep only the recording-bar animation under it.
- Reuse the orb blurred and at low opacity elsewhere for depth.
- Add light movement or overlay depth to the backgrounds (soft glows and a slow light sweep).
- Extend to **60 s** for reading time.
- Keep the exact style.

**My choice:** the hands-holding-a-phone image was left out, because Kalam is Mac-only.

### 6.5 Lively cut, 60 s (`scenes-lively.html`)

**Asked:**
- More dynamic, youthful and lively.
- Background elements, movement and overlays are allowed.
- Duration and aspect ratio locked.

**Corrections after the first draft:**
- Too many elements. Remove the rounded rectangles and keep only the recording-icon waves and the stars.
- More dynamic slide transitions.
- Arabic in the same colour as the English, with no second font.
- More 3D.

**Built:**
- 3D swing transitions.
- Cards flying in from depth, results flipping up, chips turning in.
- Camera orbit.
- Half as many sparkles and waves.

### 6.6 Dynamic cut, 60 s, final (`scenes-dynamic.html`)

**Asked:**
- Animation like the two reference cuts ("Sara" and "Halima"), but on your backgrounds and buttons.
- Background overlay: only the recording icon, very big, blurred and low opacity. No other icons.
- An orange background with the same noise as the others.
- Wait for the remaining backgrounds.

**Scene backgrounds:**

| Scene | Background |
|---|---|
| Still typing | Hands glow |
| Key press | Orange fill |
| Any app | Orange clouds |
| Arabic + English | Person with beam |
| Smart touches | Orange glow, sky, diagonal |
| Bilingual app | Soft sky |
| Privacy | Blue glow under a night tint |
| End card | Megaphone, with white text |

**Corrections:**
- Replace the orange frame's background with the image you attached. "Changed your mind mid speaking?" moved onto the person-writing image.
- The "brief" frame goes on the next image you attached. "No ums. No uhs." moved onto the pastel gradient.
- Privacy chip: change only the Arabic from «بلا سحابة» to **«بياناتك في جهازك»**. **Keep the English "No cloud" exactly as it is.**
- File size must never force lower quality. Share it by link instead of chat.

**Also changed:** the beat pulse was removed, with a top-quality export (CRF 16, AAC 320 kbps) and safer audio peaks.

**Delivered:** `promo-videos` branch, 76 MB.

### 6.7 Arabic promo, 10 sections, 66 s, final (`scenes-ar.html`, brief in `SCRIPT-AR.md`)

**Asked:**
- Rebuild in 10 sections, matching your 21-artboard storyboard read left to right, top to bottom.
- Two separate videos, Arabic and English. Make **the Arabic one only** now.
- Section 10 (the outro) stays as it is, with the English removed.
- Burst animation on chosen sections.
- The original recording bar everywhere.
- It can run over one minute.
- Deliver by download link.

**Final copy (with the hamza and shadda you approved):**

| # | Section | Caption |
|---|---|---|
| 1 | Still typing | لين الحين تكتب؟ |
| 2 | Hold Right ⌥ | اضغط مطوّل على [⌥ اليمين] واشرح. → تفكّه وينكتب على طول |
| 3 | Any app | يشتغل في أي تطبيق |
| 4 | Both languages | يدعم ويفهم اللغتين |
| 5 | Change your mind | غيّرت رأيك وأنت تتكلم → كلام يفهمك ويعدّل |
| 6 | Shortcuts | ضيّف اختصاراتك |
| 7 | No fillers | يحذف «إمم» و«آه» تلقائي |
| 8 | Interface | واجهة عربية أو إنجليزية |
| 9 | Private and local | كل اللي تقوله يبقى في جهازك. → chips: بدون حساب · بدون اشتراك · يشتغل أوفلاين |
| 10 | Outro | Unchanged, without the English |

**Copy corrections:**
- «يشتغل في **أي** تطبيق», not «في تطبيق».
- Section 5 says «تتكلم» (speaking), not «تكتب» (writing).
- Section 9 items are shown as three chips.
- Hamza and shadda added where they apply.

**Section-by-section direction:**

| Section | Direction |
|---|---|
| 1 + 2 | As in the calm cut you liked. Arabic-only captions in black. The caption key becomes a **black chip with white text**. The original recording bar. **Transition 1 → 2:** the circle reveal from your reference, with the key pressing, white rings and the section 2 glow spreading from the key. |
| 3 | `bg/sky-peach.png`. Each card lands with a burst. **Slack replaced with X.** WhatsApp icon corrected to the real mark. |
| 4 | `bg/blue-bars.webp`. Bubbles flat coral with a tail and **no shadow**. Standard recording bar. Glass EN/AR toggle kept. Dialect chips made glass like the toggle. |
| 5 | `bg/diagonal-soft.webp`. Result button **rounded with a slight soft shadow**. |
| 6 | Same background and screen as before. Beat 1: zoom in on the top menu, with a magnifier on the Shortcuts icon. Beat 2: pan right to the window's end and magnify "Best regards,". |
| 7 | Same background. Instead of removing the line, **scale it down and move it to the top**, then type "The brief is ready." underneath in bold, with no empty middle. Burst on the pill. |
| 8 | `bg/blue-clear.webp`. The same animation as the "Halima" video's bilingual section (screens dealt like cards, then a 3D flip EN → AR), with **a burst on each screen**. |
| 9 | Your background (`bg/blue-cream.webp`). **A burst on each chip.** The new copy. |

**My choices:**
- Mockup text (email, chat, cards) stays in English.
- Section 9 chips use a teal ✓ rather than ✕, because a ✕ beside «يشتغل أوفلاين» would read as "doesn't work offline".
- No coral highlight on the Gulf and Omani chips.
- White captions on the two dark blues for readability.

**Delivered:** `promo-videos` branch, 79 MB.

### 6.8 Install reel, 76 s, final (`scenes-install.html`)

**Asked:**
- Turn the install screen recording into a reel in the same style.
- Minimal background.
- Cut away the windows and the permission clutter.
- Show only the important clicks.
- Use magnifier effects, cut-outs, cursor or click indicators and highlights.
- No duration limit. Vertical.

**Built** (the recording was 640×404, too soft to magnify, so every window was rebuilt as a crisp mockup with its wording copied exactly):

| Step | Time | Content |
|---|---|---|
| Intro | 0–4 s | Icon, "Install Kalam / طريقة تثبيت كلام", "8 quick steps" |
| 1 | 4–10 s | Double-click Kalam.dmg in Downloads |
| 2 | 10–16 s | Drag Kalam into Applications; the folder lights up and bursts |
| 3 | 16–24 s | "Kalam Not Opened", zoom in on **Done**, with a "Normal the first time" note |
| 4 | 24–32 s | Privacy & Security, with a zoom and spotlight on **Open Anyway** |
| 5 | 32–40 s | Confirm **Open Anyway**, then **Use Password…**, with a "Touch ID works too" note |
| 6 | 40–50 s | Keystroke Receiving, Open System Settings, the Input Monitoring toggle turns on, Quit & Reopen |
| 7 | 50–58 s | Accessibility toggle |
| 8 | 58–64 s | Microphone, **Allow** |
| Ready | 64–72 s | Right ⌥, the recording bar, "Hello, hello, testing." typed into a note |
| End | 72–76 s | Logo and taglines |

- Every click has a moving cursor, a coral ripple and a click sound.
- Small targets get a camera zoom and spotlight.
- The mockups fade out under the captions.
- Captions are bilingual, because the macOS UI is in English.

**Delivered:** `promo-videos` branch, about 101 MB.

### 6.9 Film-style intro, 49 s, final (`scenes-film.html`): motion and post only

**Asked:**
- Animate the approved silhouette stills per the film brief, in a realism style.
- The Kalam icon popping with a brand glow.
- Very clear and minimal, showing the problem (writing takes long) and the solution (just say it).
- Vertical, no duration limit.
- Highest quality on GitHub, not in chat.

**Constraint:** no image-to-video tool was available, so motion is virtual camera work on the stills, with all UI composited in post.

| Shot | Still | Camera | Post-production |
|---|---|---|---|
| 1 Typing (0–6 s) | Close typing frame | Slow dolly in | Draft card types slowly, with a typo and backspaces; the same text on the laptop screen |
| 2 Stall (6–9.6 s) | Plate, hands lifted | Locked, handheld | Text deleted and retyped, caret blinks |
| 3 Discovery (9.6–13.8 s) | Screen glows coral | Locked, slight push | Kalam icon pops with a coral glow and rings, flies into the screen; the real Kalam home window opens |
| 4 Hold and speak (13.8–18.6 s) | Macro finger on key | Slow push | Key glow pulse and ring, "Right ⌥" chip, original recording bar, "You say" card |
| 5 Let go (18.6–23.2 s) | Leaning back, release | Locked | Full message lands at once; screen filled; "Typed where your cursor is" pill |
| 6 Correction (23.2–27.8 s) | Same still | Slow dolly in | "3, no wait," highlighted and struck through, then "Meet at 4." |
| 7 Private (27.8–32 s) | Over-the-shoulder screen | Locked | Recording bar on the screen's pill; "Works offline" chip |
| 8 Free (32–36 s) | Hands behind head | Slow dolly back | Caption only |
| 9 Swaps (36–42.4 s) | Khaliji, Levantine, English, Omani | One continuous scale-in | Freeze-cuts with a white flash and shutter tick; dialect card and screen line (RTL for Arabic) |
| 10 End (42.4–49 s) | Brand gradient | Blur-out of the last shot | Icon with glow, wordmark, both taglines |

**Technique:**
- Stills upscaled 1.1× with sharpening.
- Each laptop screen mapped as a measured quad.
- Hand mattes keep fingers in front of the UI.
- Animated grain over everything.

**Captions:** the seven captions from your brief, plus two problem captions and all the Arabic lines, which I wrote and flagged for your review.

**Follow-up:** you asked for the script without any on-screen text and with the multi-person scene removed, as a downloadable MD. That's `promo/FILM-SCRIPT.md`, which has 9 scenes and the swap sequence as an optional suggested ending.

---

## 7. Standing rules (all corrections combined)

1. Never invent features. Use only `KALAM.md`.
2. Arabic is right to left, natural and Gulf-friendly. Add hamza and shadda where they apply.
3. **Arabic uses the same colour and weight as English.** One font family.
4. **Use the original Kalam recording bar** everywhere (dark capsule, 11 bars orange → yellow → blue).
5. Less bounce, no beat pulse, minimal background elements. If there's an overlay, it's only the recording icon, large, blurred and low opacity.
6. Keep your exact wording where you specify it, such as the English "No cloud" and the Arabic «بياناتك في جهازك».
7. Wait for all files and your approval before rendering when you say so.
8. Top quality always. Deliver by GitHub link, never compressed to fit the chat.
9. Vertical 1080×1920 for everything after the first video.

---

## 8. Production pipeline

| Stage | Tool | Detail |
|---|---|---|
| Scenes | HTML/CSS/JS page per cut (`promo/scenes-*.html`) | Deterministic `renderAt(t)`, `DURATION`, `CUES` |
| Frames | Playwright + Chromium (`promo/render.mjs`) | Modes `frames` (JPEG q95 at 30 fps), `stills` (PNG previews or poster), `cues` (sound-cue JSON) |
| Film prep | `promo/film_prep.py` | Upscale, screen quads, hand mattes |
| Music | `promo/music_*.py` (numpy synthesis, no samples) | Tracks and SFX timed from page cues |
| Audio master | ffmpeg | `loudnorm I=-15 TP=-3`, then `alimiter limit=0.5`, then AAC |
| Video encode | ffmpeg libx264 | `-preset slow`, CRF 16 (film CRF 14), yuv420p, High profile, `+faststart`, AAC 320 kbps 48 kHz |
| Build | `promo/build.sh <mode>` | Modes: (default), `vertical`, `calm`, `lively`, `dynamic`, `ar`, `install`, `film`. Writes `brag-output/<name>.mp4` plus a poster. |

---

## 9. Delivery

**Why GitHub:** the chat upload limit is 30 MB. Early drafts were squeezed under it (CRF 21–23), but you asked never to compromise quality. Finals are therefore committed to a separate orphan branch, **`promo-videos`**, which holds only the videos, posters and a README table. GitHub accepts files up to 100 MB.

| File | Link |
|---|---|
| Dynamic cut | https://github.com/amiraceen/Dictation_app/raw/promo-videos/kalam-promo-vertical-dynamic.mp4 |
| Arabic promo | https://github.com/amiraceen/Dictation_app/raw/promo-videos/kalam-promo-ar.mp4 |
| Install reel | https://github.com/amiraceen/Dictation_app/raw/promo-videos/kalam-install.mp4 |
| Film intro | https://github.com/amiraceen/Dictation_app/raw/promo-videos/kalam-film.mp4 |
| All files | https://github.com/amiraceen/Dictation_app/tree/promo-videos |

The repo has since moved to **`amiraceen/Kalam`**. GitHub redirects the old links; the new form is `https://github.com/amiraceen/Kalam/raw/promo-videos/<file>`.

**Source:** everything is on branch `claude/keen-sagan-1f9tn2` under `promo/`. Rebuild any cut with `./promo/build.sh <mode>`.

**Checks before every delivery:**
- Frames from every scene and mid-transition were reviewed.
- Exact duration confirmed.
- Loudness checked at about −15 to −16.5 LUFS, with the true peak below 0 dBTP (the film peaks at −4.8 dB).

---

## 10. Edge cases and open items

- **Audio is unheard.** The soundtracks were measured, not listened to. Listen before posting.
- **Shortcuts screenshot typo:** "Ceen → ceen markting" is visible in the zoomed shots. Re-take the screenshot to fix it.
- **Third-party logos:** WhatsApp and X marks appear in the Arabic cut. Check you're comfortable using them before publishing.
- **Arabic mockup text:** the email, chat and card text in the Arabic cut is still in English.
- **English 10-section version:** planned but not built yet.
- **Film:**
  - The macro key is printed "alt/cmd", so it's labelled "Right ⌥" in post.
  - The stills are 768 px wide, so they're slightly soft when upscaled.
  - The problem captions and the dialect lines need a native-speaker check.
- **Install reel** is close to the 100 MB per-file limit. A longer version would need slightly higher compression or Git LFS.

## 11. Accessibility and readability

- Captions sit in the top third, clear of the Reels and TikTok UI at the bottom and right.
- Contrast: ink text on light backgrounds, white text with a soft shadow on photos and dark blues. Frosted cards keep text off busy areas.
- Reading time: scenes were lengthened to 60–66 s at your request so viewers can read both languages.
- Arabic uses proper RTL layout and real Arabic type (Readex Pro). It isn't mirrored Latin.
- No voiceover. All meaning is carried by the captions and UI, so the videos work with the sound off.
