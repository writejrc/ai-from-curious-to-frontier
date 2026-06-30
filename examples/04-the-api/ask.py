"""ask.py — the chat box, but now your program can use it.

This is the smallest possible thing: send a question in code, get an answer back. No website,
no human clicking. Once it lives in a script, it can run any time, in a loop, on a schedule,
while you sleep. That is the whole point of the API.

    export OPENROUTER_API_KEY=sk-or-...
    python ask.py "explain a database index like I am 10"
"""

import os
import sys
from openai import OpenAI

MODEL = os.getenv("DIARY_MODEL", "google/gemini-2.5-flash-lite")

if not os.getenv("OPENROUTER_API_KEY"):
    sys.exit("Set OPENROUTER_API_KEY first (see the README). Nothing was sent.")

question = " ".join(sys.argv[1:]).strip() or "Give me one simple tip to get better at coding."

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])
response = client.chat.completions.create(
    model=MODEL,
    max_tokens=400,
    messages=[{"role": "user", "content": question}],
)
print(response.choices[0].message.content)
