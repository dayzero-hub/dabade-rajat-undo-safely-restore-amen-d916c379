"""A tiny stock list. Small on purpose — the point is the git workflow, not this code."""

import json
from pathlib import Path

CONFIG = Path(__file__).with_name("config.json")


def load():
    return json.loads(CONFIG.read_text())


def in_stock(items):
    return [i for i in items if i["count"] > 0]


def main():
    cfg = load()
    items = cfg["items"]
    print(f"{cfg['shop']} — {len(in_stock(items))} of {len(items)} lines in stock")
    for i in in_stock(items):
        print(f"  {i['name']:<12} {i['count']:>3}")


if __name__ == "__main__":
    main()
