#!/usr/bin/env bash
pip3 install pyyaml requests python-telegram-bot

python scripts/tracker.py
python scripts/issues.py
