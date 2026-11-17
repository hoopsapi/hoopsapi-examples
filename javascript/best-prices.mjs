// Best available moneyline for every upcoming game, across all bookmakers. Node 18+, no dependencies.
//   HOOPSAPI_KEY=... node best-prices.mjs NBA
const competition = process.argv[2] ?? "NBA";
const res = await fetch(`https://hoopsapi.com/api/v1/games?competition=${encodeURIComponent(competition)}`, {
  headers: { Authorization: `Bearer ${process.env.HOOPSAPI_KEY}` },
});
if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
const { games } = await res.json();
for (const g of games) {
  const books = Object.entries(g.periods.ft ?? {}).filter(([, m]) => m.moneyline);
  if (!books.length) continue;
  const best = (side) => books.reduce((a, b) => (b[1].moneyline[side] > a[1].moneyline[side] ? b : a));
  const [hb, hm] = best("home");
  const [ab, am] = best("away");
  console.log(`${g.start_time.slice(0, 16)}  ${g.home} ${hm.moneyline.home} (${hb})  v  ${g.away} ${am.moneyline.away} (${ab})`);
}
