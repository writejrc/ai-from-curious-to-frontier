# Chapter 5 — Answers a Program Can Use

A paragraph is for humans; your code needs **data**. Ask for JSON, get clean fields you can
drop into a calendar, sheet, or database.

## Run it
```bash
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
export OPENROUTER_API_KEY="sk-or-..."
python extract.py
```
It turns a messy email into `{name, company, date, time, phone, asks}`. **Make it yours:**
change `EMAIL` and the field list.
