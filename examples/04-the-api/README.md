# Chapter 4 — When the Chat Box Runs Out

A website is fine until you want AI to run **on its own**. The "API" is just the chat box your
*code* can call: send a question from a script, get the answer back in your program.

## Run it
```bash
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
export OPENROUTER_API_KEY="sk-or-..."
python "ask.py \"explain a database index like I am 10\""
```
Once the answer is in your code, you can save it, sort it, email it, or run it on a timer.
