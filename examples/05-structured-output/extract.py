"""extract.py — get DATA back, not a paragraph.

A paragraph is nice for a human. But my code can't use a paragraph. It needs clean fields.
So I ask the model to reply only as JSON, then I load it like any other data. Now the answer
can go straight into a calendar, a database, a spreadsheet — whatever I want.

    export OPENROUTER_API_KEY=sk-or-...
    python extract.py
"""

import os
import sys
import json
from openai import OpenAI

MODEL = os.getenv("DIARY_MODEL", "google/gemini-2.5-flash-lite")

if not os.getenv("OPENROUTER_API_KEY"):
    sys.exit("Set OPENROUTER_API_KEY first (see the README). Nothing was sent.")

EMAIL = """Hi, this is Priya from Acme. We'd like to move our call to Friday 4 July at 11am.
My number is 98765 43210. Can you also send the pricing for the Pro plan? Thanks."""

prompt = f"""Read this email and return ONLY a JSON object, nothing else, with these keys:
name, company, requested_date, requested_time, phone, asks (a list of short strings).
If a field is missing, use null.

Email:
{EMAIL}"""

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])
response = client.chat.completions.create(
    model=MODEL,
    max_tokens=400,
    response_format={"type": "json_object"},   # ask for clean JSON
    messages=[{"role": "user", "content": prompt}],
)

raw = response.choices[0].message.content
data = json.loads(raw)            # now it's real data my program can use
print("Loaded as a Python object:\n")
print("  name   :", data.get("name"))
print("  company:", data.get("company"))
print("  when   :", data.get("requested_date"), data.get("requested_time"))
print("  phone  :", data.get("phone"))
print("  asks   :", data.get("asks"))
print("\nFull JSON:\n", json.dumps(data, indent=2, ensure_ascii=False))
