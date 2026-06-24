"""A tiny first build: an AI agent that reads the internet and tells you what matters.

This is the cleaned-up version of the "fifteen ugly lines" from the post — same idea,
just readable. It pulls a couple of feeds, asks a model which items are worth your time,
and prints a digest. Clone it, run it, break it, make it yours.

Uses OpenRouter (one key, any model). It's OpenAI-compatible, so we use the `openai` SDK
pointed at OpenRouter.

    export OPENROUTER_API_KEY=sk-or-...
    python digest.py
"""

import os
import sys
import feedparser
from openai import OpenAI

# --- Make it yours: edit these. ---
FEEDS = [
    "https://hnrss.org/frontpage",                 # Hacker News front page
    "https://simonwillison.net/atom/everything/",  # Simon Willison — practical AI/engineering
]
WHAT_I_CARE_ABOUT = "practical AI engineering, agents that run in production, and shipping"
MODEL = os.getenv("DIARY_MODEL", "google/gemini-2.5-flash-lite")  # cheap + fast (verified); override w/ DIARY_MODEL or swap here

# The #1 first-run failure is a missing key. Fail with a human message, not a traceback.
if not os.getenv("OPENROUTER_API_KEY"):
    sys.exit("Set OPENROUTER_API_KEY first (see the README). Nothing was sent.")

# 1. Grab the latest headlines from each feed (a handful each — keep it cheap).
items = []
for url in FEEDS:
    feed = feedparser.parse(url)
    if not feed.entries:
        print(f"!  No items from {url} (feed down or URL changed) — skipping.", file=sys.stderr)
    for entry in feed.entries[:8]:
        items.append(f"- {entry.title} ({entry.link})")

if not items:
    sys.exit("No headlines fetched from any feed. Check your FEEDS list and your internet.")

headlines = "\n".join(items)

# 2. Ask the cheapest model that does the job: "which of these matter to me?"
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])
response = client.chat.completions.create(
    model=MODEL,
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": (
            f"I care about: {WHAT_I_CARE_ABOUT}.\n\n"
            f"Today's headlines:\n{headlines}\n\n"
            "Pick only the ones genuinely worth my time. For each: the title and one "
            "sentence on why it matters. If nothing qualifies, say so plainly."
        ),
    }],
)

# 3. Print the digest. (The real version writes it to a file and notifies me at 8am.)
print(response.choices[0].message.content)
