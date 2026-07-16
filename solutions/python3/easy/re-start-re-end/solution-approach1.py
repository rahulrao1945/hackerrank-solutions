# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
# Problem     Re.start() & Re.end()
# Difficulty  Easy
# Subdomain   Regex and Parsing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-16, 09:32 a.m.
# ──────────────────────────────────────────────────

import re

s = input()
k = input()

found = False

for m in re.finditer(r'(?={})'.format(re.escape(k)), s):
    print((m.start(), m.start() + len(k) - 1))
    found = True

if not found:
    print((-1, -1))
