# Chapter 1 — The Starting Line

The smallest real thing I built: an agent that reads the internet and tells me what matters.

This is the cleaned-up version of *the fifteen ugly lines* from the post — the seed of an
agent I now run at 8am every day. It's deliberately tiny. The code was never the point; the
point was that I ran it, changed it, and felt the difference between *consuming* AI content
and *building* with it. If you want to feel that too, it's yours.

## Run it

```bash
uv venv && source .venv/bin/activate          # or: python -m venv .venv && source .venv/bin/activate
uv pip install -r requirements.txt            # or: pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."         # your key; never commit it
python digest.py
```

You should get back a short, opinionated digest of today's headlines — filtered to what
*you* said you care about.

## Now break it (this is the assignment)

- Change `WHAT_I_CARE_ABOUT` to your actual interests. Re-run. Watch the digest change.
- Swap the `FEEDS` for ones you read. (Any RSS/Atom URL works.)
- Make the prompt meaner: "be ruthless, keep at most 3."
- Print it to a file instead of the screen. Congratulations — that's 80% of a real cron job.

## What this taught me

1. An LLM call is just a function: text in, text out. No magic.
2. Routine work runs fine on a cheap, fast model on purpose (`claude-haiku-4-5`) — more in Chapter 4.
3. It stopped being a tutorial and started being *mine* the moment I changed a line and re-ran it.

A full run costs a fraction of a cent. Run it ten times while you tinker.

## Troubleshooting

- **`Set ANTHROPIC_API_KEY first ...`** — you haven't set the key in *this* terminal.
  Run the `export` line again (it doesn't persist across new windows).
- **`No items from <url> ...`** — that feed is down or its URL changed. The script skips it
  and keeps going; if *every* feed fails it stops and tells you. The two default feeds
  (Hacker News, Simon Willison) were confirmed working when this shipped.
- **`ModuleNotFoundError`** — your virtual env isn't active, or deps aren't installed.
  Re-run the two setup lines above.
