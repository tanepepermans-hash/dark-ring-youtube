# The Dark Ring — Content Operating System

Faceless YouTube-kanaal over echte, geverifieerde dark stories uit de bokswereld
(criminaliteit, controverses, rechtszaken, schandalen). AI-ondersteund, maar met
menselijke goedkeuring op de punten die er echt toe doen: feiten, rechten, kwaliteit
en publicatie.

**Lees eerst [`PLAN.md`](./PLAN.md)** — dat is de volledige audit, de toolstack-keuzes,
de workflow met goedkeuringsstappen, en het MVP-voorstel. Dit README is alleen de
snelstart/structuur-uitleg.

## Structuur

| Map | Inhoud |
|---|---|
| `content-database/` | `content_db.csv` — de centrale tracking-tabel per video, plus `schema.md` |
| `tools/` | `content_db.py` — command-line tool om rijen toe te voegen/bijwerken (geen dependencies, geen API-key) |
| `prompts/` | Herbruikbare AI-prompts, één per pipeline-stap (idea → research → fact-check → script → visual plan → metadata) |
| `templates/` | Markdown-sjablonen: script, QC-checklist, metadata |
| `research/` | Per-video researchdossier, bestandsnaam `<id>.md` |
| `scripts/` | Per-video voice-over script, bestandsnaam `<id>.md` |
| `voiceovers/` | Audiobestanden per video (gitignored — binair) |
| `assets/` | Geselecteerde stock/beeld per video (gitignored) |
| `projects/` | Werkmap per video: shotlist, editing-notities |
| `exports/` | Afgeronde videobestanden (gitignored) |
| `thumbnails/` | Thumbnail-bestanden |
| `published/` | Metadata-snapshot van live video's |
| `analytics/` | Periodieke analytics-samenvattingen |

Zie `NAMING_CONVENTIONS.md` voor de ID-conventie (`DR-0001`, etc.) en bestandsnamen.

## Snelstart: content-database gebruiken

```bash
# nieuw onderwerp toevoegen (status wordt automatisch "idea")
python tools/content_db.py add --title "Working title" --category court-case --hook "..."

# alle video's met een bepaalde status tonen
python tools/content_db.py list --status research

# status/veld bijwerken
python tools/content_db.py update DR-0001 --field fact_check_status --value verified
```

Geen dependencies nodig — puur Python-stdlib (`csv`, `argparse`), werkt met elke
Python 3-installatie.

## Belangrijk

Er is in deze fase **geen enkele betaalde API aangesloten**. `.env.example` laat zien
welke keys later relevant worden (bv. ElevenLabs, YouTube Data API) zodra we die stap
samen zetten — vul die uitsluitend in via een lokale `.env`-file (nooit hardcoded, nooit
gecommit; zie `.gitignore`).
