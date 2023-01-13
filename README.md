# cron-parser

## Environment Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to run

```bash
python3 main.py "your argument"
```
Argument Format: "cron expression command"\n
Cron Expression Format: minutes hours days_of_month month days_of_week, allowed special characters: *, /, -, , .


## Tests

To run unit test, use the following command:

```bash
pytest
```
