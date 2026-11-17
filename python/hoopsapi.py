"""Minimal HoopsAPI client: one function, standard library only. Set HOOPSAPI_KEY first."""
import json
import os
import urllib.parse
import urllib.request

BASE = "https://hoopsapi.com/api/v1"


def get(path, **params):
    """GET an endpoint, e.g. get("/games", competition="NBA"). Returns the parsed JSON."""
    key = os.environ.get("HOOPSAPI_KEY")
    if not key:
        raise SystemExit("Set HOOPSAPI_KEY (free key at https://hoopsapi.com/sign-up)")
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(f"{BASE}{path}" + (f"?{query}" if query else ""), headers={"Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)
