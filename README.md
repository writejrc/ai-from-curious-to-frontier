# From AI-curious to the frontier — a hands-on field guide

I went from not knowing what a token was to building AI systems that run unattended. This
repo is the companion to a LinkedIn series where I document my journey — the actual code I
wrote at each step is here, yours to take.

**This is hands-on, not theory.** It isn't a course, and I'm not teaching — it's the code
from my climb, posted as I go. Clone it, run it, break it; that's how it stuck for me. If
you want dry concepts from a podium, this will disappoint you — that's the point.

> **Status:** I'm posting this live as I climb — no fixed schedule, no finish line. The
> code fills in here episode by episode (Chapter 1 is in). Star/watch to catch each drop.

I'm not selling anything. It's just my path, written down. If you see yourself in it, maybe
it becomes yours too.

## Using it

1. Grab whichever chapter you're on — each example stands alone.
2. `cd examples/NN-<name>/`, read its README, run it, then change it.
3. Break it on purpose. Fix it. That's how it stuck for me.

## The climb (open-ended)

Roughly the shape of it. No fixed length — each part is the wall the last one ran into, and
the code lands here as I get to it. Starts here:

1. **Making it do one real thing** — [`examples/01-starting-line/`](examples/01-starting-line/) is the first build
2. **Stop reinventing** — using what already exists instead of building from scratch
3. **Demo → something that survives** — reliability, when "seems fine" isn't enough
4. **Letting it run on its own** — agents, and learning to trust them
5. **Cost, secrets, shipping** — the unglamorous stuff that makes it real
6. **Building with AI** — not just building it
7. **Staying in it** — and onward, because the ground keeps shifting

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
| **An API key** — I use [OpenRouter](https://openrouter.ai/keys) (one key, any model) | Paid — pennies | The examples call a model through OpenRouter. A full run costs a fraction of a cent. |

The only true prerequisite money can't buy: **ten minutes and a willingness to break things.**

## Setup (once)

```bash
export OPENROUTER_API_KEY="sk-or-..."   # never commit this
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

These examples call a **cheap, fast model through OpenRouter** (one key, any model — the
`MODEL` line at the top of each script; default `google/gemini-2.0-flash-lite-001`). Routine
work doesn't need the biggest model. A full run costs a fraction of a cent, and you can swap
the model in one line. (Chapter 4 is entirely about this choice.)

## License

MIT — see [LICENSE](LICENSE). Take the code, use it, ship something.
