#!/usr/bin/env python3
"""Command-line tool for content-database/content_db.csv. Stdlib only, no API keys."""

import argparse
import csv
import sys
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "content-database" / "content_db.csv"

FIELDS = [
    "id", "title", "subject_person", "category", "sources", "fact_check_status",
    "hook", "script_status", "voiceover_status", "assets_status", "edit_status",
    "video_title", "thumbnail_status", "publish_date", "youtube_url", "views",
    "retention_pct", "subscribers_gained", "revenue", "status", "notes",
]


def read_rows():
    if not DB_PATH.exists() or DB_PATH.stat().st_size == 0:
        return []
    with DB_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_rows(rows):
    with DB_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in FIELDS})


def next_id(rows):
    numbers = []
    for row in rows:
        rid = row.get("id", "")
        if rid.startswith("DR-"):
            try:
                numbers.append(int(rid.split("-")[1]))
            except (IndexError, ValueError):
                pass
    return f"DR-{(max(numbers) + 1) if numbers else 1:04d}"


def cmd_add(args):
    rows = read_rows()
    new_row = {field: "" for field in FIELDS}
    new_row["id"] = next_id(rows)
    new_row["title"] = args.title
    new_row["category"] = args.category or ""
    new_row["hook"] = args.hook or ""
    new_row["subject_person"] = args.subject_person or ""
    new_row["status"] = "idea"
    new_row["fact_check_status"] = "pending"
    new_row["script_status"] = "pending"
    new_row["voiceover_status"] = "pending"
    new_row["assets_status"] = "pending"
    new_row["edit_status"] = "pending"
    new_row["thumbnail_status"] = "pending"
    rows.append(new_row)
    write_rows(rows)
    print(f"Added {new_row['id']}: {new_row['title']}")


def cmd_list(args):
    rows = read_rows()
    if args.status:
        rows = [r for r in rows if r.get("status") == args.status]
    if not rows:
        print("(no matching rows)")
        return
    for row in rows:
        print(f"{row['id']}\t[{row['status']}]\t{row['title']}")


def cmd_update(args):
    rows = read_rows()
    for row in rows:
        if row.get("id") == args.id:
            if args.field not in FIELDS:
                sys.exit(f"Unknown field '{args.field}'. Valid fields: {', '.join(FIELDS)}")
            row[args.field] = args.value
            write_rows(rows)
            print(f"Updated {args.id}: {args.field} = {args.value}")
            return
    sys.exit(f"No row found with id '{args.id}'")


def main():
    parser = argparse.ArgumentParser(description="Manage content_db.csv")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new video idea")
    p_add.add_argument("--title", required=True)
    p_add.add_argument("--category")
    p_add.add_argument("--hook")
    p_add.add_argument("--subject-person", dest="subject_person")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="List rows, optionally filtered by status")
    p_list.add_argument("--status")
    p_list.set_defaults(func=cmd_list)

    p_update = sub.add_parser("update", help="Update a single field on a row")
    p_update.add_argument("id")
    p_update.add_argument("--field", required=True)
    p_update.add_argument("--value", required=True)
    p_update.set_defaults(func=cmd_update)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
