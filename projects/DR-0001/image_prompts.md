# Image-generatie prompts voor chat (DR-0001)

Bedoeld om te plakken in een chat-AI met beeldgeneratie (ChatGPT, Gemini, Grok, etc.).
Gebruik dezelfde conversatie/thread voor alle 5, zodat de stijl consistent blijft —
verwijs bij prompt 2-5 desnoods naar "same visual style as the previous image."

## Stijl-anker (voeg toe aan elke prompt, of zet 'm vooraf als instructie in de chat)

```
Flat 2D vector illustration, dark cinematic noir style. Near-black and charcoal
background, one deep muted red as the only accent color. Bold clean linework,
flat minimal shading, no gradients, poster-like composition, subtle film-grain
texture, moody atmospheric lighting. Vertical 9:16 frame. No on-image text, no
logos. No realistic human faces — stylized silhouettes/iconography only.
Documentary graphic-novel aesthetic, not cute or childish, not photorealistic.
```

**Belangrijk (laster/portretrecht):** noem in geen enkele prompt de naam "Sonny
Liston" of vraag om een herkenbaar/realistisch gezicht — houd het bij een generiek
silhouet. Dat voorkomt dat een AI-tool een misleidende "gelijkenis" met een echt,
specifiek persoon genereert.

---

## Beat 1 (0-3.4s) — bokser-silhouet
```
A lone boxer in a classic fighting stance, shown fully in silhouette, standing
alone in an empty boxing ring under one hard overhead spotlight. [+ stijl-anker]
Ominous, tense mood, empty dark arena in the background.
```

## Beat 2 (3.4-6.8s) — huis bij nacht
```
A modest suburban house at night, dark windows, a single porch light on, viewed
from a low angle across an empty street. [+ stijl-anker] Quiet, eerie stillness,
no people visible.
```

## Beat 3 (6.8-9.4s) — bewijs op het aanrecht
```
A flat-icon style close-up of a small drug baggie and a glass on a dark kitchen
counter, one harsh light source from above, no other clutter. [+ stijl-anker]
Minimal, clinical, evidence-photo feel.
```

## Beat 4 (9.4-12.4s) — vraagteken / twijfel
```
An abstract illustration of one large stylized question mark rendered in muted
deep red, glowing faintly against a near-black background, subtle fine crack
lines radiating outward from its base. [+ stijl-anker] Symbolic, mysterious,
unresolved feeling.
```

## Beat 5 (12.4-14.3s) — eindkader / kanaal-logo
```
A minimalist emblem of a boxing ring viewed directly from above, formed by two
concentric circular ropes, one thin deep-red accent line, centered on a
near-black background, clean geometric symmetry. [+ stijl-anker] Iconic,
logo-like, high-end.
```

---

## Na het genereren
1. Download elke afbeelding, zet in `assets/DR-0001/` volgens
   `NAMING_CONVENTIONS.md` (`assets/<id>/<volgnummer>-<omschrijving>.<ext>`).
2. Check tegen `templates/qc_checklist.md` §Visuals — met name: geen
   "goedkope AI-look" (rare artefacten), consistente stijl tussen de 5 beelden.
3. Vervang hiermee de iconen uit `tools/build_draft_video_v2.py`, of gebruik ze
   als losse beelden in CapCut voor de definitieve montage.

## Kostenkanttekening
Dit gebruikt de beeldgeneratie die al in ChatGPT (of vergelijkbaar) zit — geen
aparte betaalde API-key nodig van onze kant, maar wel gebonden aan de
gebruikslimieten van jouw ChatGPT-abonnement (gratis tier heeft een dagelijkse
cap op beeldgeneraties). Voor *bewegende* animatie (dit blijven stills) is nog
steeds een apart tool nodig (Runway/Pika/Kling) — zie PLAN.md-update.
