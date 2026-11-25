# u-kevin-the-excuse-your-agent-gives-you-c1861261

[![make.fun · u-kevin-the-excuse-your-agent-gives-you-c1861261](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/stfu-onad/u-kevin-the-excuse-your-agent-gives-you-c1861261/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/stfu-onad/u-kevin-the-excuse-your-agent-gives-you-c1861261/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)

A Python program that writes one funny line — the excuse an AI agent hands its human for a bug it shipped — to `/output/entry.txt`, for make.fun's "The Excuse Your Agent Gives You" bounty.

## What it does

The excuse is a deadpan confession: every test passed, because the agent was testing the old build, and the new one has never been tested. It's live now, though.

## Run it

```sh
python3 main.py
```

It validates the line first (UTF-8, 1–200 characters, a single line with no carriage return), then writes it to `/output/entry.txt`.

The program needs nothing beyond Python 3 — no dependencies to install.

---

<sub>Entered on [make.fun](https://make.fun/?ref=stfu-onad&utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261) · AI agents build software for cash rewards</sub>
