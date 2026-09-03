# Naming conventions

## Video-ID

Formaat: `DR-0001`, `DR-0002`, ... (`DR` = The Dark Ring). Opeenvolgend, nooit hergebruikt
(ook niet als een video wordt geschrapt — zet dan `status` op `dropped` in de database).
`tools/content_db.py add` genereert dit automatisch als volgende vrije nummer.

## Bestandsnamen (per video, overal dezelfde `<id>`)

| Map | Bestand |
|---|---|
| `research/` | `<id>.md` |
| `scripts/` | `<id>.md` |
| `voiceovers/` | `<id>.mp3` |
| `projects/` | `<id>/shotlist.md`, `<id>/notes.md` |
| `assets/` | `<id>/<volgnummer>-<korte-omschrijving>.<ext>` |
| `exports/` | `<id>.mp4` (definitieve export) |
| `thumbnails/` | `<id>.png` |
| `published/` | `<id>.md` (metadata-snapshot: titel, beschrijving, tags, publicatiedatum, URL) |
| `analytics/` | `<jaar>-<maand>.md` (maandelijkse samenvatting over alle video's) |

## Categorieën (kolom `category` in content_db.csv)

Gebruik één van: `criminal-case`, `controversy`, `organized-crime`, `court-case`,
`mystery`, `career-derailed`, `historical-scandal`, `behind-the-fight`, `corruption`,
`rivalry`, `tragedy`, `untold-story`. Nieuwe categorie toevoegen mag, maar hou het
consistent (voeg 'm hier toe zodra je een nieuwe gebruikt).

## Statussen (kolom `status` — de hoofd-workflowstatus)

`idea` → `research` → `fact-checked` → `scripted` → `voiced` → `visual-planned` →
`assets-ready` → `edited` → `qc-passed` → `published` (of `dropped`/`on-hold` op elk
moment).

Deelstatussen (`fact_check_status`, `script_status`, `voiceover_status`, `assets_status`,
`edit_status`, `thumbnail_status`) gebruiken telkens: `pending`, `in-progress`, `done`,
`needs-revision`.
