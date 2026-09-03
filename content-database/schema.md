# content_db.csv — kolomuitleg

Eén rij per video (Short of long-form). Bewerk via `tools/content_db.py`, niet
handmatig in een spreadsheet-programma dat de CSV-opmaak kan wijzigen (bv. Excel kan
UTF-8/komma's stukmaken) — Google Sheets/Numbers openen is prima om te *bekijken*.

| Kolom | Betekenis | Voorbeeldwaarde |
|---|---|---|
| `id` | Uniek video-ID, zie `NAMING_CONVENTIONS.md` | `DR-0001` |
| `title` | Werktitel (kan afwijken van uiteindelijke YouTube-titel) | `The night that ended his career` |
| `subject_person` | Bokser(s)/persoon/personen waar het verhaal om draait | `Jack Doe` |
| `category` | Eén van de vaste categorieën, zie naming conventions | `court-case` |
| `sources` | Bronnen, `;`-gescheiden (URL's of citaten) | `nyt.com/...; court-record-1987` |
| `fact_check_status` | `pending` / `in-progress` / `verified` / `needs-revision` | `verified` |
| `hook` | De 0–3 sec hookzin | `This fight was never supposed to happen.` |
| `script_status` | `pending` / `in-progress` / `done` / `needs-revision` | `done` |
| `voiceover_status` | `pending` / `in-progress` / `done` | `done` |
| `assets_status` | `pending` / `in-progress` / `done` | `in-progress` |
| `edit_status` | `pending` / `in-progress` / `done` | `pending` |
| `video_title` | Definitieve YouTube-titel | `He Was Never Supposed to Fight That Night` |
| `thumbnail_status` | `pending` / `in-progress` / `done` / `n/a` (Shorts hebben er vaak geen nodig) | `n/a` |
| `publish_date` | ISO-datum, leeg tot gepland | `2026-09-10` |
| `youtube_url` | Live URL, leeg tot gepubliceerd | |
| `views` | Handmatig of via Analytics API bijgewerkt | `0` |
| `retention_pct` | Gemiddeld % bekeken | |
| `subscribers_gained` | Subs gewonnen via deze video | |
| `revenue` | Indien van toepassing | |
| `status` | Hoofd-workflowstatus, zie `NAMING_CONVENTIONS.md` | `research` |
| `notes` | Vrije tekst: lessons learned, twijfels, redactionele kanttekeningen | |
