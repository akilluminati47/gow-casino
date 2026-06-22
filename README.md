# GOW Casino — Emergence Casino

A *Gears of War*–themed casino floor. Fan project, for entertainment only — no real wagering.

## Floor

- **Emergence Reels** (`slot-machine.html`) — a 5×3, 9-line slot with three free-spin bonus rounds (COG Assault, Locust Horde, Lambent Surge).
- **The Table Pit** (`table-games.html`) — Blackjack, Baccarat, Three Card Poker, Horde Hold'em, Jacks-or-Better Video Poker, and WAR, dealt from the 52-card Sera deck.
- **Full Deck Preview** (`card-preview.html`) — the complete Sera deck artwork.

One shared, browser-stored wallet runs across the whole floor.

## Run

Pure static HTML/CSS/JS — open `index.html` in a browser, or serve the folder:

```bash
python -m http.server 8000
```

## Assets

`make_favicons.py` regenerates the favicon set from `images/favicon.png` (the skull-gear emblem) using Pillow.

---

*Gears of War © The Coalition / Microsoft.* Fan project by [Δ47](https://guns.lol/akilluminati47).
