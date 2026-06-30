# Chapter 6 — Don't Learn the Tool, Scout It

There is no "best" model — only the right one for today, and it changes monthly. One key
(OpenRouter), many models, easy to swap. This asks the same question to a few models.

## Run it
```bash
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
export OPENROUTER_API_KEY="sk-or-..."
python compare_models.py
```
**Note:** outputs vary on purpose — when this was written, two models gave clear answers and
one returned nonsense. That *is* the lesson: try a few, keep what works, swap one word when a
model dies. **Make it yours:** edit the `MODELS` list.
