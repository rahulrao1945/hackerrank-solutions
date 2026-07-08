# ──────────────────────────────────────────────────
# Problem     Write a function
# Difficulty  Medium
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-08, 05:58 p.m.
# ──────────────────────────────────────────────────

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

