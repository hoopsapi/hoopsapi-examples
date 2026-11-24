# HoopsAPI examples

Examples for [HoopsAPI](https://hoopsapi.com), a basketball odds API: moneyline, handicap (spread) and totals from multiple bookmakers (Pinnacle, FanDuel, Unibet, Betway, Smarkets, 1xBet), for the NBA, NCAA, EuroLeague and 100+ other competitions, with quarter and half lines and full price history.

Every example uses only the standard library. Get a free API key at [hoopsapi.com/sign-up](https://hoopsapi.com/sign-up) (no credit card), then:

```bash
export HOOPSAPI_KEY=your_key
```

## Quick start

```bash
curl -H "Authorization: Bearer $HOOPSAPI_KEY" "https://hoopsapi.com/api/v1/games?competition=NBA"
```

Each game has every bookmaker's main lines, by period (`ft`, `h1`, `h2`, `q1`–`q4`):

```json
{
  "game_id": 1639747022,
  "competition": "NBA",
  "home": "Chicago Bulls",
  "away": "Philadelphia 76ers",
  "start_time": "2026-11-17T01:00:00Z",
  "periods": {
    "ft": {
      "pinnacle": {
        "moneyline": { "home": 3.45, "away": 1.33 },
        "spread": { "line": 8.5, "home": 1.91, "away": 1.99 },
        "total": { "line": 229.5, "over": 1.95, "under": 1.94 }
      },
      "fanduel": { "...": "..." }
    }
  }
}
```

`spread.line` is the home team's handicap: `8.5` means the home team gets 8.5 points.

## Examples

| Example | What it does | Plan |
|---|---|---|
| [python/best_prices.py](python/best_prices.py) | Best moneyline for each game across all bookmakers | Free |
| [javascript/best-prices.mjs](javascript/best-prices.mjs) | The same in Node 18+ | Free |
| [python/value_vs_pinnacle.py](python/value_vs_pinnacle.py) | Removes Pinnacle's margin to get fair odds, then lists prices elsewhere that beat them | Free |
| [python/line_movement.py](python/line_movement.py) | Opening vs latest price at each bookmaker, from a game's full price history | Data |
| [python/download_season.py](python/download_season.py) | Downloads a month of bulk data: every price change from every bookmaker | Data |

```bash
cd python
python3 best_prices.py NCAA
python3 value_vs_pinnacle.py "Europe - Euroleague"
```

Competition names come from `GET /api/v1/competitions`.

## Use it from an AI assistant (MCP)

[![HoopsAPI MCP connector](https://glama.ai/mcp/connectors/com.hoopsapi/basketball-odds/badges/score.svg)](https://glama.ai/mcp/connectors/com.hoopsapi/basketball-odds)

HoopsAPI has a remote MCP server at `https://hoopsapi.com/mcp`, using the same API key. In Claude Code:

```bash
claude mcp add --transport http --scope user hoopsapi https://hoopsapi.com/mcp \
  --header "Authorization: Bearer YOUR_API_KEY"
```

Then ask things like *"What are the best prices for tonight's NBA games?"*. Setup for Claude, ChatGPT, Codex and GitHub Copilot: [hoopsapi.com/ai](https://hoopsapi.com/ai).

## Endpoints

| Endpoint | |
|---|---|
| `GET /api/v1/competitions` | Competitions with upcoming games |
| `GET /api/v1/games?competition=NBA` | Upcoming games with every bookmaker's main lines |
| `GET /api/v1/games/{id}` | One game with every alternate line; closing odds once it has started |
| `GET /api/v1/games/{id}/history` | Every price change for a game (Data plan) |
| `GET /api/v1/discrepancies` | Biggest gaps between bookmakers (Pro and Data plans) |
| `GET /api/v1/providers` | Bookmakers and when each was last updated |
| `GET /api/v1/exports` | Bulk monthly files (Data plan) |

Full reference: [hoopsapi.com/docs](https://hoopsapi.com/docs) · [OpenAPI spec](https://hoopsapi.com/openapi.json) · [Pricing](https://hoopsapi.com/pricing)

## Further reading

- [How to remove the bookmaker margin from odds](https://hoopsapi.com/guides/remove-bookmaker-margin)
- [Closing line value: what it is and how to measure it](https://hoopsapi.com/guides/closing-line-value)
- [How much do basketball odds differ between bookmakers?](https://hoopsapi.com/guides/compare-basketball-odds)
- [Historical basketball odds data (bulk downloads)](https://hoopsapi.com/historical-data)

## License

MIT
