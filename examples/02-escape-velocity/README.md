# Chapter 2 — Escape Velocity

The move that finally got me out of tutorial hell: stop building toy projects, pick one real
thing I did by hand all the time, and automate it — then actually use it.

`explain.py` is mine. Paste an error, get a plain-English explanation and the smallest fix. I
built it because I was pasting errors into a chat window twenty times a day. Now it's one
command, and I use it constantly. That's the whole point — a tiny thing you *keep*.

## Run it

```bash
uv venv && source .venv/bin/activate          # or: python -m venv .venv && source .venv/bin/activate
uv pip install -r requirements.txt            # or: pip install -r requirements.txt
export OPENROUTER_API_KEY="sk-or-..."         # your key; never commit it
python explain.py "TypeError: 'NoneType' object is not subscriptable"
```

Or pipe a real crash straight in:

```bash
python some_script_that_breaks.py 2>&1 | python explain.py
```

**What it actually printed** (real run, OpenRouter + `gemini-2.5-flash-lite`, trimmed):

```
1. What it means: you're trying to access an item inside something that doesn't hold any
   items. Like grabbing the "second apple" from an empty bowl.
2. Most likely cause: you expected a list/dict but got None — often a function that was
   supposed to return a collection returned None instead.
3. Smallest fix: check for None before you index.
   if my_variable is not None:
       first_item = my_variable[0]
```

Verified end-to-end against the real model. Run it on your own errors.

## The assignment (this is how you actually escape)

Don't just run mine. **Ship your own.** It takes one sitting:

1. **Pick ONE thing you keep doing by hand.** Pasting errors into a chatbot. Rewriting the
   same kind of message. Summarizing something. Cleaning up messy notes. Anything real.
2. **Copy `explain.py` and change two things:** the prompt, and what it takes as input.
   That's genuinely most of it.
3. **Run it on a real example from your actual day** — not a toy one.
4. **Use it again tomorrow.** The day you reach for a thing you built instead of doing it by
   hand, you've hit escape velocity. That's the post.

## Make it yours (ideas)
- `rewrite.py` — paste text, get it in your voice / tone.
- `tldr.py` — paste a long thing, get the 3 bullets that matter.
- `commit.py` — pipe `git diff`, get a commit message.

## Troubleshooting
- **`Set OPENROUTER_API_KEY first ...`** — set the key in this terminal (it doesn't persist
  across new windows).
- **`ModuleNotFoundError`** — virtual env isn't active, or deps aren't installed; re-run the
  two setup lines.

A full run costs a fraction of a cent. Break it on purpose.
