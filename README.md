# From AI-curious to the frontier — a hands-on field guide

I went from not knowing what a token was to building autonomous AI systems that run
unattended. This repo is the companion to a LinkedIn series where I document the climb —
and hand you the actual, runnable code at each step.

**This is hands-on, not theory.** Every module ships a small, self-contained example you
can clone, run, and break. You learn AI by building, not by nodding along. If you want dry
concepts from a podium, this will disappoint you — that's the point.

I'm not selling anything. If one person gets unstuck because of this, it was worth it.

## How to use this repo

1. Pick the module you're on (they build, but each example stands alone).
2. `cd examples/NN-<name>/`, read its README, run it, then change it.
3. Break it on purpose. Fix it. That's the whole method.

## The curriculum

| # | Module | What you'll be able to do | Code |
|---|--------|---------------------------|------|
| 1 | The Starting Line | Locate where you are; ship the smallest real thing | [`examples/01-starting-line/`](examples/01-starting-line/) |
| 2 | Escape Velocity | Get out of tutorial hell by shipping | _coming_ |
| 3 | Don't Learn the Tool, Scout It | Discover + compose existing capabilities | _coming_ |
| 4 | Where 90% Quit | Tell a demo from a system; design for failure | _coming_ |
| 5 | Delegate, Then Verify | Run the human–agent loop | _coming_ |
| 6 | Staying at the Frontier | Build a compounding learning system | _coming_ |

## Prerequisites — the AI-builder's starter bench

You do **not** need to be a developer. You need a small set of basic, mostly-free tools.
This isn't a random shopping list — it's the standard bench for working with AI the right
way, and you'll reuse it for everything in this series and beyond. Everything here is free
except the API key, which costs pennies.

| Tool | Cost | Why it's on the bench (the best practice) |
|------|------|-------------------------------------------|
| **A terminal** — Terminal (macOS/Linux) or PowerShell/WSL (Windows) | Free, built in | Real work happens here. Opening it is the bar. |
| **A code editor** — [VS Code](https://code.visualstudio.com/), or an AI-native one like [Cursor](https://cursor.com/) | Free / free tier | Where you read and change code. AI-native editors let you pair with a model as you go. |
| **Git** + a free [GitHub account](https://github.com/signup) | Free | Version control is your undo button — and how you learn in public. (No git? Download this repo as a ZIP from the green **Code** button.) |
| **Python 3.10+** with [uv](https://docs.astral.sh/uv/) | Free | `python3 --version` to check; [install Python](https://www.python.org/downloads/). `uv` keeps each project's packages isolated — a best practice from day one, and far faster than pip. |
| **An AI coding assistant** — [Claude Code](https://www.claude.com/product/claude-code), or the AI built into your editor | Free tier / paid | The "work with the machine" muscle. You'll lean on this more every module. |
| **An Anthropic API key** — from [console.anthropic.com](https://console.anthropic.com/) | Paid — pennies | The examples call Claude. A full run costs a fraction of a cent. |

The only true prerequisite money can't buy: **ten minutes and a willingness to break things.**

## Setup (once)

```bash
export ANTHROPIC_API_KEY="sk-ant-..."   # never commit this
```

Each example has its own `requirements.txt`. With `uv` you can spin up an isolated env per
example in seconds:

```bash
cd examples/01-starting-line
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
```

(Plain `python -m venv .venv && pip install -r requirements.txt` works too.)

## A note on cost

These examples use **Claude Haiku 4.5** (`claude-haiku-4-5`) — Anthropic's fastest, cheapest
model — because routine work doesn't need the biggest model. A full run of the Module 1
example costs a fraction of a cent. (Module 4 is entirely about this choice.)

## License

MIT — see [LICENSE](LICENSE). Take the code, use it, ship something.
