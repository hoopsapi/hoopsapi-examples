"""How a game's moneyline moved at each bookmaker, from opening to now (or to the close). Needs the Data plan.

    python3 line_movement.py GAME_ID
Game ids come from best_prices.py or GET /games.
"""
import sys

from hoopsapi import get

game_id = sys.argv[1]
h = get(f"/games/{game_id}/history", market="moneyline", period="ft", limit=5000)
print(f"{h['home']} v {h['away']} ({h['competition']}), {h['count']} price changes\n")
by_book = {}
for c in reversed(h["changes"]):  # the API returns newest first
    by_book.setdefault((c["provider"], c["outcome"]), []).append(c)
for (book, outcome), cs in sorted(by_book.items()):
    print(f"{book:10} {outcome:5} opened {cs[0]['price']:.2f} ({cs[0]['at'][:16]})  latest {cs[-1]['price']:.2f} ({cs[-1]['at'][:16]})  {len(cs)} changes")
