"""The fifteen ugly lines that became my 8am agent.

It reads a few feeds, asks Claude which items actually matter to me,
and prints a digest. That's it. Clone it, run it, break it, make it yours.

Run:  ANTHROPIC_API_KEY=sk-ant-... python digest.py
"""

import os
import feedparser
import anthropic

# Edit these two to make it yours.
FEEDS = [
    "https://hnrss.org/frontpage",          # Hacker News front page
    "https://www.anthropic.com/rss.xml",     # Anthropic news
]
WHAT_I_CARE_ABOUT = "practical AI engineering, agents that run in production, and shipping"

# 1. Grab the latest headlines from each feed (a handful each — keep it cheap).
items = []
for url in FEEDS:
    for entry in feedparser.parse(url).entries[:8]:
        items.append(f"- {entry.title} ({entry.link})")
headlines = "\n".join(items)

# 2. Ask the cheapest model that does the job: "which of these matter to me?"
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
response = client.messages.create(
    model="claude-haiku-4-5",    # fast + cheap — routine triage doesn't need the biggest model
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": (
            f"I care about: {WHAT_I_CARE_ABOUT}.\n\n"
            f"Here are today's headlines:\n{headlines}\n\n"
            "Pick only the ones genuinely worth my time. For each, give the title and "
            "one sentence on why it matters. If nothing qualifies, say so."
        ),
    }],
)

# 3. Print the digest. (The real version writes a file and notifies me at 8am.)
print(next(block.text for block in response.content if block.type == "text"))
