"""explain.py — paste an error, get a plain-English explanation and the smallest fix.

The tool I built to climb out of tutorial hell. Instead of staying stuck, I made the thing
that gets me unstuck — and now I use it every day. Tiny, a little ugly, mine. That's escape
velocity: not another tutorial, one real thing you actually keep.

    export ANTHROPIC_API_KEY=sk-ant-...
    python explain.py "TypeError: 'NoneType' object is not subscriptable"
    # or pipe a real crash straight in:
    python some_script.py 2>&1 | python explain.py
"""

import os
import sys
import anthropic

# The #1 first-run failure is a missing key. Fail with a human line, not a traceback.
if not os.getenv("ANTHROPIC_API_KEY"):
    sys.exit("Set ANTHROPIC_API_KEY first (see the README). Nothing was sent.")

# Take the error from the command line, or from a pipe.
error_text = " ".join(sys.argv[1:]).strip() or sys.stdin.read().strip()
if not error_text:
    sys.exit('Give me an error, e.g.  python explain.py "IndexError: list index out of range"')

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
response = client.messages.create(
    model="claude-haiku-4-5",   # cheap + fast — right for a tool you hit all day long
    max_tokens=600,
    messages=[{
        "role": "user",
        "content": (
            "I'm learning to code and just hit this error. In plain English, give me: "
            "(1) what it means, (2) the most likely cause, (3) the smallest fix. "
            "Be concise and concrete — no lecture.\n\n"
            f"{error_text}"
        ),
    }],
)
print(next(b.text for b in response.content if b.type == "text"))
