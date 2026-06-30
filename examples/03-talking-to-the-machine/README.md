# Chapter 3 — Talking to the Machine

The first AI skill is not picking a tool. It is **how you ask**. This runs the *same* messy
note through a lazy prompt ("Summarize this") and a clear, specific one, so you can see the gap.

## Run it
```bash
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
export OPENROUTER_API_KEY="sk-or-..."
python prompt_compare.py
```
The clear prompt gives a clean, numbered, ready-to-use list. Same model, better words.
**Make it yours:** change `NOTE` and `CLEAR` to a real task of yours.
