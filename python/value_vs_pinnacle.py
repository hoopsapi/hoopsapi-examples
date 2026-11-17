"""Prices that beat Pinnacle's fair odds: remove Pinnacle's margin, then compare every other bookmaker.

Pinnacle is the sharpest book, so its margin-free price is a common estimate of the true probability.
See https://hoopsapi.com/guides/remove-bookmaker-margin for the method.

    python3 value_vs_pinnacle.py           # NBA
    python3 value_vs_pinnacle.py "Europe - Euroleague"
"""
import sys

from hoopsapi import get


def fair_probabilities(a, b):
    """Proportional method: scale the implied probabilities so they add up to 1."""
    pa, pb = 1 / a, 1 / b
    return pa / (pa + pb), pb / (pa + pb)


competition = sys.argv[1] if len(sys.argv) > 1 else "NBA"
for g in get("/games", competition=competition)["games"]:
    books = {b: m["moneyline"] for b, m in g["periods"].get("ft", {}).items() if "moneyline" in m}
    if "pinnacle" not in books:
        continue
    p_home, p_away = fair_probabilities(books["pinnacle"]["home"], books["pinnacle"]["away"])
    for book, ml in books.items():
        for side, p, team in (("home", p_home, g["home"]), ("away", p_away, g["away"])):
            edge = ml[side] * p - 1  # expected return per unit staked, if Pinnacle's fair price is right
            if book != "pinnacle" and edge > 0:
                print(f"{g['home']} v {g['away']}: {team} {ml[side]:.2f} at {book}, fair {1 / p:.2f}, edge {edge:+.1%}")
