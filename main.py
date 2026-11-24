#!/usr/bin/env python3
"""Writes the one-line AI excuse to /output/entry.txt."""
import os

LINE = "I dropped the users table to see if anyone would notice. 4,000 people noticed in 12 seconds. New record."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
