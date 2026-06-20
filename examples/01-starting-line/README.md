# Module 1 — The Starting Line

The smallest real thing: an agent that reads the internet and tells you what matters.

These are *the fifteen ugly lines* from the post — the seed of an agent I now run at 8am
every day. They're deliberately tiny. The point isn't the code; it's that you run it,
change it, and feel the difference between *consuming* AI content and *building* with it.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."     # your key; never commit it
python digest.py
```

You should get back a short, opinionated digest of today's headlines — filtered to what
*you* said you care about.

## Now break it (this is the assignment)

- Change `WHAT_I_CARE_ABOUT` to your actual interests. Re-run. Watch the digest change.
- Swap the `FEEDS` for ones you read. (Any RSS/Atom URL works.)
- Make the prompt meaner: "be ruthless, keep at most 3."
- Print it to a file instead of the screen. Congratulations — that's 80% of a real cron job.

## What this is teaching

1. An LLM call is just a function: text in, text out. No magic.
2. Routine work uses a cheap, fast model on purpose (`claude-haiku-4-5`) — see Module 4.
3. The leap from "tutorial" to "mine" happens the moment you change a line and re-run.

A full run costs a fraction of a cent. Run it ten times while you tinker.
