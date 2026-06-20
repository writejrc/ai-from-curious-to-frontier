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

## Setup (once)

You'll need Python 3.10+ and an Anthropic API key.

```bash
export ANTHROPIC_API_KEY="sk-ant-..."   # never commit this
```

Each example has its own `requirements.txt`. Use a fresh virtual env per example.

## A note on cost

These examples use **Claude Haiku 4.5** (`claude-haiku-4-5`) — Anthropic's fastest, cheapest
model — because routine work doesn't need the biggest model. A full run of the Module 1
example costs a fraction of a cent. (Module 4 is entirely about this choice.)

## License

MIT — see [LICENSE](LICENSE). Take the code, use it, ship something.
