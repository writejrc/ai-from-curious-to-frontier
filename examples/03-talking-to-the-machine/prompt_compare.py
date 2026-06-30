"""prompt_compare.py — see why HOW you ask changes WHAT you get.

Same messy note, two prompts: a lazy one and a clear one. Run it and read both answers.
The gap between them is the whole skill. (And later: even the clear prompt has limits.)

    export OPENROUTER_API_KEY=sk-or-...
    python prompt_compare.py
"""

import os
import sys
from openai import OpenAI

MODEL = os.getenv("DIARY_MODEL", "google/gemini-2.5-flash-lite")

if not os.getenv("OPENROUTER_API_KEY"):
    sys.exit("Set OPENROUTER_API_KEY first (see the README). Nothing was sent.")

NOTE = """call dr fix re: knee monday or tue morning, get the form from HR before that,
and tell ravi the demo moved to thursday 3pm not wednesday. also pay the electricity bill."""

LAZY = f"Summarize this:\n\n{NOTE}"

CLEAR = f"""Read this messy note and pull out the action items.
Return a short numbered list. Each item: what to do, and any date/time, in plain words.
If something has no date, just say "no date".

Note:
{NOTE}"""

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])

def ask(prompt):
    r = client.chat.completions.create(model=MODEL, max_tokens=400,
                                       messages=[{"role": "user", "content": prompt}])
    return r.choices[0].message.content

print("=== LAZY PROMPT ('Summarize this') ===\n")
print(ask(LAZY))
print("\n=== CLEAR PROMPT (specific, with a format) ===\n")
print(ask(CLEAR))
