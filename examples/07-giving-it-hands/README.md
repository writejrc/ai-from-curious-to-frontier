# Chapter 7 — Giving It Hands

A model is a word machine, not a calculator. Give it **tools** and it can *do* things. Here it
gets a calculator tool, decides to use it, and answers correctly.

## Run it
```bash
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
export OPENROUTER_API_KEY="sk-or-..."
python tool_use.py
```
Real run: the model called `calculate("1234*5678+99")` and answered 7,006,751.
**Note:** tool/function calling needs a capable model (default `openai/gpt-4o-mini`).
