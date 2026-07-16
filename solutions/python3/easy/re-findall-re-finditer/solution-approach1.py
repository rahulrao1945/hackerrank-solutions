# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true
# Problem     Re.findall() & Re.finditer()
# Difficulty  Easy
# Subdomain   Regex and Parsing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-16, 09:31 a.m.
# ──────────────────────────────────────────────────

import re

s = input()

matches = re.findall(r'(?<=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])([aeiouAEIOU]{2,})(?=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])', s)

if matches:
    print("\n".join(matches))
else:
    print(-1)
