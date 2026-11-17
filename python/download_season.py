"""Download a month of bulk odds data (every price change, every bookmaker) and read it. Needs the Data plan.

    python3 download_season.py                # lists the files
    python3 download_season.py nba 2026-11    # downloads one month
"""
import gzip
import json
import os
import sys
import urllib.request

from hoopsapi import BASE, get

if len(sys.argv) < 3:
    print(json.dumps(get("/exports"), indent=2))
    raise SystemExit
league, month = sys.argv[1], sys.argv[2]
path = f"{league}-{month}.ndjson.gz"
req = urllib.request.Request(f"{BASE}/exports/{league}/{month}.ndjson.gz", headers={"Authorization": f"Bearer {os.environ['HOOPSAPI_KEY']}"})
with urllib.request.urlopen(req, timeout=300) as r, open(path, "wb") as f:
    f.write(r.read())
with gzip.open(path, "rt") as f:
    games = [json.loads(line) for line in f]  # one game per line
books = {c["bookmaker"] for g in games for c in g["changes"]}
print(f"Saved {path}: {len(games)} games, {sum(len(g['changes']) for g in games)} price changes from {', '.join(sorted(books))}")
