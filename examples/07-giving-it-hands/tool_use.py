"""tool_use.py — let the model DO things, not just talk.

A model is good with words, but bad at exact maths (and it can't check the weather, or read
your database). So you hand it tools. Here we give it one tool: a calculator. We ask a hard
sum, the model decides to call the tool, our code runs the real calculation, and the model
uses that result to answer. That hand-off is how an AI stops chatting and starts acting.

Note: tool/function calling needs a model that supports it (gpt-4o-mini does).

    export OPENROUTER_API_KEY=sk-or-...
    python tool_use.py
"""

import os
import re
import sys
import json
from openai import OpenAI

MODEL = os.getenv("DIARY_MODEL", "openai/gpt-4o-mini")

if not os.getenv("OPENROUTER_API_KEY"):
    sys.exit("Set OPENROUTER_API_KEY first (see the README). Nothing was sent.")

def calculate(expression: str) -> str:
    if not re.fullmatch(r"[\d\s+\-*/().]+", expression):   # only numbers and math symbols
        return "error: not a plain math expression"
    return str(eval(expression, {"__builtins__": {}}, {}))  # safe-ish: no builtins, digits only

tools = [{
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Do exact arithmetic. Pass a plain expression like 1234*5678.",
        "parameters": {"type": "object",
                       "properties": {"expression": {"type": "string"}},
                       "required": ["expression"]},
    },
}]

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ["OPENROUTER_API_KEY"])
messages = [{"role": "user", "content": "What is 1234 * 5678 plus 99? Use the calculator tool."}]

resp = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)
msg = resp.choices[0].message

if msg.tool_calls:
    print("The model asked to use a tool:")
    messages.append({"role": "assistant", "content": msg.content, "tool_calls": [
        {"id": tc.id, "type": "function",
         "function": {"name": tc.function.name, "arguments": tc.function.arguments}}
        for tc in msg.tool_calls]})
    for tc in msg.tool_calls:
        args = json.loads(tc.function.arguments)
        result = calculate(args["expression"])
        print(f"  → calculate({args['expression']!r}) = {result}")
        messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})
    final = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    print("\nFinal answer:\n" + final.choices[0].message.content)
else:
    print("(The model answered without the tool — try a model that supports tool calling.)")
    print(msg.content)
