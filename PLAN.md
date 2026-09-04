# The Dark Ring — Audit & Technisch Plan

Status: **concept-audit, nog niet geïmplementeerd**. Dit document is de eerste opdracht:
een kritische beoordeling + een concreet plan. Er is nog geen enkele API aangesloten en
er wordt nog geen content geproduceerd. Dat gebeurt pas na jouw akkoord, per onderdeel.

> Disclaimer over actualiteit: mijn kennis heeft een cutoff (januari 2026) en tool-prijzen/
> -features veranderen snel. Alle genoemde prijzen/limieten zijn richtwaarden — controleer
> ze zelf op de site van de tool voordat je een abonnement neemt. Ik geef geen omzetgaranties.

> **Update na de eerste pilot (DR-0001):** de visuele stijl is bijgesteld van "premium
> documentaire met stockbeeld/tekstkaarten" (oorspronkelijke brief, §6) naar
> **animatie/motion-graphics, en korter (15-25 sec i.p.v. 35-60 sec)**. Belangrijke
> consequentie: echte, vloeiende cartoon-animatie (bewegende personages/gezichten)
> vereist een betaalde AI-videotool (Runway/Pika/Kling, kosten per generatie) of een
> animatie-abonnement (bv. Vyond) — dat is nog niet aangesloten. Wat nu wél gratis/lokaal
> werkt: vlakke, symbolische iconen (silhouetten, geen afbeelding van een specifiek echt
> persoon) die in beeld "poppen" via zelfgebouwde Python/ffmpeg-tooling
> (`tools/build_draft_video_v2.py`). Dit is de tussenoplossing totdat we samen beslissen
> of een betaalde tool de investering waard is.

---

## 1. Kritische beoordeling van het concept

**Wat werkt:**
- Boxing + "echte, controleerbare verhalen" is een sterkere niche-keuze dan generieke
  "dark stories" kanalen. True crime / mysterie-kanalen zijn extreem verzadigd; boksen
  als subniche met documentaire-kwaliteit is minder bezet.
- De discipline om alleen geverifieerde feiten te gebruiken is zowel een kwaliteits- als
  een *monetisatie*-voordeel (zie §6) en een differentiator t.o.v. AI-slop-kanalen.
- Shorts-eerst om format/hook te valideren voordat je in long-form investeert is de juiste
  volgorde — long-form kost veel meer tijd per stuk output.

**Wat ik kritisch wil markeren (dingen die het plan onderschat):**
1. **Bronnenprobleem is het echte knelpunt, niet de techniek.** Voor "onbekende
   verhalen uit de boksgeschiedenis" met echte namen/data heb je betrouwbare bronnen nodig
   (rechtbankverslagen, kranten uit die tijd, biografieën, gerenommeerde sportjournalistiek).
   AI-research (Claude/Perplexity) kan dit versnellen maar **verzint soms bronnen of
   details die plausibel klinken**. Fact-check kan daarom niet worden geautomatiseerd tot
   "AI zegt het is correct" — het moet altijd een menselijke check tegen minimaal 2
   onafhankelijke, citeerbare bronnen zijn voordat een video live gaat. Dit is de
   belangrijkste bottleneck van het hele systeem, niet editing of voice-over.
2. **Beeldmateriaal is het grootste copyright/kwaliteitsrisico.** Je wilt geen gestolen
   fight-footage en geen goedkope AI-look. Dat betekent in de praktijk: je hebt bijna nooit
   *echte* foto's/footage van de bokser in kwestie tot je beschikking (die zijn vaak
   copyrighted, ook oude persfoto's). Realistische aanpak: bouw beelden op met generieke,
   licentievrije boksring/gym/stad/archief-sfeerbeelden (Pexels/Pixabay/Mixkit), documenten/
   krantenkoppen als grafisch element, kaarten, tijdlijnen, en subtiele, consistente
   motion-graphics — niet met AI-gegenereerde "gezichten" van echte, herkenbare personen
   (portretrecht/smaad-risico, zie §6).
3. **Laster/portretrecht-risico bij levende of recent overleden personen.** "Criminaliteit
   rond bekende boksers" en "controverses" raakt al snel aan beschuldigingen over echte,
   soms nog levende mensen. Elke claim moet ofwel (a) uit de rechtszaak/veroordeling zelf
   komen, of (b) expliciet gebracht worden als "beschuldiging/aantijging", nooit als feit.
   Dit is een redactionele regel, geen technische — zet 'm in de QC-checklist (zie §8).
4. **"Zo min mogelijk handmatig werk" en "premium documentaire-kwaliteit" trekken in
   tegengestelde richting.** Volledig geautomatiseerde video-assemblage levert op dit
   moment (nog) geen premium documentaire-editing — camera-timing, muziekkeuze, pacing
   van een goede hook. De grootste ROI zit in het automatiseren van de *repetitieve* stappen
   (research-aggregatie, transcript, captions, metadata, uploaden, analytics) en het
   **handmatig doen van de paar stappen die smaak vereisen** (finale edit-pass, thumbnail,
   welke hook). Dat is ook precies jouw eigen principe #18 — dit plan volgt dat consequent.
5. **1 short/dag bij 5 uur/week is krap maar haalbaar** als je batcht: research en scripts
   voor een hele week in één sessie, dan een vaste editing-workflow met een sjabloon.
   Reken realistisch op ~20–30 min actieve tijd per Short zodra het sjabloon staat
   (niet de eerdere 15 min-aanname, en zeker niet 0 min).

**Conclusie:** het concept is goed, mits je (a) research/fact-check als het echte werk
behandelt i.p.v. als iets dat "AI wel even doet", en (b) in de eerste maand vooral het
*format* valideert met een klein aantal handmatig geproduceerde video's, voordat je iets
automatiseert.

---

## 2. Wat is anno nu realistisch te automatiseren?

| Stap | Automatiseerbaar? | Wie/wat | Mens nodig? |
|---|---|---|---|
| Idea generation | Grotendeels | Claude/ChatGPT genereert onderwerp-longlist | Jij kiest welke onderwerpen we uitwerken |
| Research | Deels | Claude (+evt. Perplexity) verzamelt bronnen/feiten | **Ja — verplicht**, verifieer bronnen |
| Fact-check | Deels (assist) | AI checkt interne consistentie, jij checkt bronnen | **Ja — verplicht, blocking gate** |
| Script | Grotendeels | Claude schrijft op basis van geverifieerde research | Jij leest/keurt script goed (ook ivm laster-risico) |
| Voice-over | Volledig | ElevenLabs (of alternatief) TTS | Steekproef beluisteren op fouten/uitspraak |
| Visual plan | Grotendeels | Claude maakt shotlist op basis van script | Korte review |
| Asset selectie (stock) | Grotendeels | Script/API-matching op Pexels/Pixabay/Mixkit | Visuele check op consistentie/stijl |
| AI-visuals (optioneel) | Deels, kost geld | Runway/Pika alleen waar stock tekortschiet | Ja, kwaliteitscontrole |
| Video-edit/assemblage | **Nu nog beperkt** | Sjabloon in CapCut (handmatig) — programmatic editing (Remotion/ffmpeg) pas als format staat | **Ja, grootste handmatige stap** |
| Captions | Volledig | CapCut auto-captions of Whisper (lokaal, gratis) | Snelle leesbaarheids-check |
| Titel | Grotendeels | Claude genereert varianten | Jij kiest |
| Description | Volledig | Claude, sjabloon-gebaseerd | Steekproef |
| Thumbnail | Deels (vnl. long-form) | Canva-sjabloon + Claude-tekst | Jij, want branding/consistentie |
| Quality control | **Nee — blijft mens** | — | **Altijd jij**, zie checklist §8 |
| Upload/scheduling | Volledig (later) | YouTube Data API | Jij drukt op "approve to publish" |
| Analytics | Volledig | YouTube Analytics API | Jij interpreteert trends |
| Next content decision | Assist | AI vat analytics samen, doet voorstellen | **Jij beslist** |

Kortom: bijna elke stap kan *versneld* worden door AI, maar drie stappen blijven
hard menselijk: **fact-check, script-goedkeuring (i.v.m. laster/rechten) en finale QC
voor publicatie.** Dat is bewust zo ontworpen — het is jouw principe #18.

---

## 3. Gratis vs. betaald — realistisch kostenoverzicht (validatiefase)

**Vrijwel gratis / al aanwezig:**
- Research & script: Claude (dit abonnement) — geen extra kosten.
- Stockbeeld/video: Pexels, Pixabay, Mixkit — gratis, commercieel te gebruiken
  (licentie per site altijd zelf even nalezen, verandert soms).
- Captions: Whisper (lokaal/open source) of CapCut ingebouwde auto-captions — gratis.
- YouTube Data API + YouTube Analytics API — gratis, wel een Google Cloud-project +
  OAuth-setup nodig (eenmalig, ~15 min).
- Editing: CapCut gratis tier is voor Shorts ruim voldoende.
- Design/thumbnail: Canva gratis tier.
- Tracking/content-database: dit repo (CSV/markdown) — gratis, geen lock-in.

**Waarschijnlijk (klein) budget nodig:**
- **Voice-over (ElevenLabs):** gratis tier heeft een beperkt aantal characters/maand —
  bij 1 short/dag (~600–900 tekens script per short) loop je daar binnen enkele weken
  tegenaan. Instapabonnement is doorgaans in de orde van €5/maand. Dit is de meest
  waarschijnlijke eerste kostenpost.
- **AI-gegenereerde visuals (Runway/Pika e.d.):** alleen inzetten als stock echt
  tekortschiet (bv. sfeerbeelden van een tijdperk/locatie die niet als stock bestaan).
  Reken op betaling per generatie/credit — **niet nodig voor de MVP**, wel iets om later
  te testen als het kanaal tractie krijgt.

**Geschat budget validatiefase (eerste 20–30 video's):** €0–€10/maand
(ElevenLabs instap, de rest gratis). Dat past ruim binnen jouw €0–€30-marge.
Betaalde AI-visuals of programmatic-editing-tooling pas toevoegen als het format
bewezen is (na de eerste 20–30 Shorts, o.b.v. data — zie §9).

---

## 4. Voorgestelde toolstack (validatiefase)

| Functie | Tool | Reden |
|---|---|---|
| Research/script | Claude | Al aanwezig, sterk in lange-vorm redenering + bronnen samenvatten |
| Voice-over | ElevenLabs (gratis→instap) | Beste kwaliteit/prijs voor natuurlijke, serieuze documentaire-stem |
| Stock beeld/video | Pexels, Pixabay, Mixkit | Gratis, ruime licentie, goede kwaliteit |
| Captions | CapCut auto-captions (of Whisper lokaal als je meer controle wilt) | Gratis, snel |
| Editing | CapCut | Gratis, snel te leren, geschikt voor 9:16 Shorts |
| Thumbnail/design | Canva | Gratis tier, sjablonen voor consistente branding |
| Metadata (titel/beschrijving) | Claude | Sjabloon-gebaseerd, snel |
| Tracking | Dit repo (CSV + kleine Python-tool) | Simpel, geen extra account, geen kosten |
| Upload/analytics (fase 2, na validatie) | YouTube Data API + Analytics API | Gratis, officieel, nodig zodra je wilt automatiseren i.p.v. handmatig uploaden |

**Bewust nog niet in de stack:** Runway/Pika (AI-video), Perplexity Pro,
programmatic video-assemblage (Remotion/ffmpeg). Dit zijn goede *fase 2*-opties zodra
het format werkt en er tijd/geld te rechtvaardigen is — nu nog niet, om complexiteit en
kosten te beperken (simpel > complex).

---

## 5. Workflow-ontwerp: idee → gepubliceerde video

Elke stap hieronder heeft een status in de content-database (§8). 🔒 = verplichte
menselijke goedkeuring voordat je door mag naar de volgende stap.

1. **Idea** — Claude genereert 10–15 onderwerpen per batch (prompt: `prompts/01_idea_generation.md`) → CSV-rij per onderwerp, status `idea`.
2. 🔒 **Topic approval** — jij kiest welke onderwerpen worden uitgewerkt (status → `research`).
3. **Research** — Claude verzamelt info + bronnen per onderwerp (`prompts/02_research.md`) → bestand in `/research/<id>.md` met een bronnenlijst.
4. 🔒 **Fact-check** — jij (evt. AI-geassisteerd via `prompts/03_fact_check.md`) verifieert
   elke claim tegen minstens 2 bronnen. Status → `fact-checked` of terug naar `research`.
5. **Script** — Claude schrijft het script o.b.v. geverifieerde research
   (`prompts/04_script.md`, sjabloon `templates/script_template.md`) → `/scripts/<id>.md`.
6. 🔒 **Script approval** — jij leest het script door, met name op laster-risico en
   toon/hook-eerlijkheid (geen misleidende clickbait, zoals jij zelf al aangaf).
7. **Voice-over** — ElevenLabs genereert audio o.b.v. het goedgekeurde script →
   `/voiceovers/<id>.mp3`.
8. **Visual plan** — Claude maakt een shotlist (welk beeld bij welke script-regel,
   `prompts/05_visual_plan.md`) → `/projects/<id>/shotlist.md`.
9. **Asset selectie** — jij (of een klein zoekscript) haalt passende stock op basis van
   de shotlist uit Pexels/Pixabay/Mixkit → `/assets/<id>/`.
10. **Video edit** — jij monteert in CapCut met het vaste sjabloon (intro-stijl, font,
    kleurgrading, muziekbed) → export naar `/exports/<id>.mp4`.
11. **Captions** — auto-captions in CapCut, in de vaste stijl (leesbaar, geen overdreven
    animatie) → onderdeel van de export.
12. **Titel/description** — Claude genereert opties (`prompts/06_metadata_thumbnail.md`,
    sjabloon `templates/metadata_template.md`) → jij kiest.
13. **Thumbnail** (vooral relevant voor long-form later) — Canva-sjabloon.
14. 🔒 **Quality control** — volledige checklist (`templates/qc_checklist.md`): facts,
    legal/copyright, story, visuals, voice, captions, monetization. Alleen bij een
    volledige "pass" mag een video naar `published`.
15. **Upload/scheduling** — in de validatiefase: handmatig uploaden (5 min, en je ziet
    meteen of alles klopt). Fase 2: YouTube Data API voor geautomatiseerd inplannen.
16. **Analytics** — na 48–72 uur cijfers loggen in de content-database (retention, views,
    subs). Handmatig in validatiefase, later via YouTube Analytics API.
17. 🔒 **Next content decision** — Claude vat trends samen ("welke hooks/onderwerpen
    presteren beter"), jij beslist wat dat betekent voor de volgende batch.

---

## 6. Copyright & monetisatie — risico's en mitigatie

- **Geen fight-footage/archiefbeeld hergebruiken** zonder duidelijke licentie — dit is
  het grootste contentstrike/demonetisatie-risico. Bouw beelden op uit generieke stock +
  eigen grafische elementen (tijdlijnen, kaarten, documentstijl-graphics) in plaats van
  echte historische opnames.
- **YouTube's beleid tegen "reused/repetitive content"** (aangescherpt sinds 2023) vereist
  aantoonbare originele toegevoegde waarde: eigen research, eigen script, eigen narratie,
  eigen editing/analyse. Dit plan is daar expliciet op gebouwd (§5), maar **controleer de
  actuele YPP-voorwaarden zelf voor je gaat monetizen** — dit beleid kan wijzigen.
- **Portretrecht/smaad:** claims over identificeerbare, mogelijk nog levende personen
  moeten aantoonbaar uit publieke rechtbank-/persverslagen komen en als zodanig worden
  gebracht (bronvermelding, "volgens de rechtbank/aanklacht", niet als eigen beschuldiging).
  Dit hoort in de QC-checklist als blocking item, niet als suggestie.
- **Muziek:** gebruik uitsluitend royalty-free tracks met duidelijke commerciële licentie
  (bv. via CapCut's eigen bibliotheek of Mixkit) — geen bekende soundtracks.

---

## 7. Projectstructuur

```
dark-ring-youtube/
├── PLAN.md                  # dit document
├── README.md                # snelstart + uitleg structuur
├── NAMING_CONVENTIONS.md    # ID's, bestandsnamen, statussen
├── .env.example             # welke API-keys later nodig zijn (nog leeg/ongebruikt)
├── content-database/
│   ├── content_db.csv       # de tracking-database, zie §8
│   └── schema.md            # kolom-uitleg
├── tools/
│   └── content_db.py        # klein command-line tool om rijen toe te voegen/bijwerken
├── prompts/                 # herbruikbare AI-prompts per pipeline-stap
├── templates/                # markdown-sjablonen (script, QC-checklist, metadata)
├── research/                 # per-video researchdossiers (<id>.md)
├── scripts/                  # per-video voice-over scripts (<id>.md)
├── voiceovers/                # audio-bestanden (.gitignored — binair, lokaal houden)
├── assets/                    # geselecteerde stock/afbeeldingen per video (.gitignored)
├── projects/                  # per-video werkmap (shotlist, editing-notities)
├── exports/                    # afgeronde video-bestanden (.gitignored)
├── thumbnails/                  # thumbnail-bestanden
├── published/                    # metadata-snapshot van gepubliceerde video's
└── analytics/                     # periodieke analytics-exports/samenvattingen
```

Grote binaire bestanden (audio/video) worden **niet** in git bijgehouden (zie
`.gitignore`) — alleen de tekst/metadata/tracking. Zet audio/video lokaal of in een
losse cloud-opslag (bv. Google Drive) als je back-up wilt.

---

## 8. Content-database / trackingsysteem

Bewust gekozen voor een simpele **CSV-bestand** (`content-database/content_db.csv`)
i.p.v. Airtable/Notion/database: geen extra account, geen kosten, direct leesbaar,
en makkelijk door Claude Code te lezen/schrijven. Als het kanaal opschaalt kun je dit
1-op-1 importeren in Airtable/Google Sheets zonder her-structurering.

Kolommen (zie ook `content-database/schema.md`):
`id, title, subject_person, category, sources, fact_check_status, hook, script_status,
voiceover_status, assets_status, edit_status, video_title, thumbnail_status, publish_date,
youtube_url, views, retention_pct, subscribers_gained, revenue, status, notes`

Beheer via `tools/content_db.py` (puur Python-stdlib, geen dependencies, geen API-key
nodig):
```
python tools/content_db.py add --title "..." --category "court-case" --hook "..."
python tools/content_db.py list --status research
python tools/content_db.py update DR-0001 --field fact_check_status --value verified
```

---

## 9. MVP-voorstel: wat we in één weekend bouwen

**Weekend 1 (nu, dit deliverable):**
- Repo + volledige projectstructuur (klaar zodra je akkoord geeft, zie stap 10).
- Content-database + `content_db.py`.
- Alle prompts + templates + QC-checklist.
- **Geen** API-integraties, **geen** automatische video-generatie.

**Daarna, expliciet ná jouw akkoord — validatie (week 2–5):**
- 3 tot 5 Shorts **volledig handmatig** produceren mét de sjablonen/prompts (dus AI
  versnelt research/script/metadata, maar jij monteert zelf in CapCut). Doel: het format
  valideren voordat er engineering-tijd in automatisering gaat.
- Pas als het format staat en je routine hebt: overwegen om een klein stukje van de
  pipeline te automatiseren (bv. YouTube-upload via de Data API, of een lokaal caption-
  script) — één stap per keer, telkens met jouw akkoord.

Dit is bewust conservatief: eerst bewijzen dat het concept werkt met weinig video's,
dan pas investeren in automatisering van een bewezen format — niet andersom.

---

## 10. Concrete eerstvolgende actie voor jou

1. Bevestig dat deze audit/dit plan klopt met wat je voor ogen had (of geef aan wat je
   anders wilt).
2. Maak een ElevenLabs-account aan (gratis tier) — dat is de enige tool die je nu al
   nodig hebt om te beginnen; de rest (Claude, stock-sites, CapCut, Canva) is direct
   bruikbaar zonder setup.
3. Kies met mij **1 onderwerp** voor de allereerste pilot-Short (ik kan een longlist van
   10 onderwerpen genereren zodra je "ja, ga verder" zegt) — dan doorlopen we samen
   stap 1 t/m 6 van de workflow (§5) voor die ene video, zodat je het proces voelt
   voordat we het schalen.

Ik implementeer niets verder (geen research starten, geen scripts schrijven, geen API's
aansluiten) totdat je hierop reageert.
