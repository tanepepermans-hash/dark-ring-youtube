Goedgekeurd script + shotlist: <plak inhoud van scripts/<ID>.md en/of
projects/<ID>/shotlist.md>

Genereer per beat/shot een kant-en-klare image-generatie prompt voor een chat-AI
met beeldgeneratie (ChatGPT, Gemini, Grok, etc.), in de vaste kanaalstijl:

```
Flat 2D vector illustration, dark cinematic noir style. Near-black and charcoal
background, one deep muted red as the only accent color. Bold clean linework,
flat minimal shading, no gradients, poster-like composition, subtle film-grain
texture, moody atmospheric lighting. Vertical 9:16 frame. No on-image text, no
logos. No realistic human faces — stylized silhouettes/iconography only.
Documentary graphic-novel aesthetic, not cute or childish, not photorealistic.
```

Regels:
- Nooit de naam van een echt, specifiek persoon in de prompt zetten, en nooit om
  een "realistisch gezicht" vragen — alleen generieke silhouetten/symboliek.
  Dit voorkomt misleidende AI-gelijkenissen met echte mensen.
- Elke prompt moet los te gebruiken zijn maar wel de stijl-anker bevatten, zodat
  de output over meerdere generaties consistent blijft.
- Output als `projects/<ID>/image_prompts.md`, met per beat: de prompt, en een
  korte instructie waar het beeld in de shotlist/timeline past.
