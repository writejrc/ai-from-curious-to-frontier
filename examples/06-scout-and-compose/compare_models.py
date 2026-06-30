"""compare_models.py — don't marry a model. Scout and swap.

Tools and models change every month. So I stopped trying to learn one and started using a
door that opens to many: OpenRouter, one key, lots of models. This runs the same question
through a few of them and prints the answers side by side. Pick the one that fits the job.
When a model dies (mine 404'd once), you swap one word. That is the real skill: find and
combine what already exists, instead of building or memorising from scratch.

    export OPENROUTER_API_KEY=sk-or-...
    python compare_models.py
"""

import os
import sys
from openai import OpenAI

if not os.getenv("OPENROUTER_API_KEY"):
    sys.exit("Set OPENROUTER_API_KEY first (see the README). Nothing was sent.")

# A few cheap models. Edit this list — that's the whole "scouting" knob.
MODELS = [
    "google/gemini-2.5-flash-lite",
    "openai/gpt-4o-mini",
    "meta-llama/llama-3.3-70b-instruct",
]
QUESTION = "In one sentence a beginner can follow, what is an API?"

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])

for model in MODELS:
    print(f"\n=== {model} ===")
    try:
        r = client.chat.completions.create(model=model, max_tokens=120,
                                           messages=[{"role": "user", "content": QUESTION}])
        print(r.choices[0].message.content.strip())
    except Exception as e:
        print(f"(skipped — {str(e)[:80]})")
