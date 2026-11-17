"""Best available moneyline for every upcoming game in a competition, across all bookmakers.

    python3 best_prices.py            # NBA
    python3 best_prices.py "NCAA"
"""
import sys

from hoopsapi import get

competition = sys.argv[1] if len(sys.argv) > 1 else "NBA"
games = get("/games", competition=competition)["games"]
print(f"{len(games)} upcoming {competition} games\n")
for g in games:
    books = {b: m["moneyline"] for b, m in g["periods"].get("ft", {}).items() if "moneyline" in m}
    if not books:
        continue
    home = max(books, key=lambda b: books[b]["home"])
    away = max(books, key=lambda b: books[b]["away"])
    print(f"{g['start_time'][:16]}  {g['home']} {books[home]['home']:.2f} ({home})  v  {g['away']} {books[away]['away']:.2f} ({away})")
