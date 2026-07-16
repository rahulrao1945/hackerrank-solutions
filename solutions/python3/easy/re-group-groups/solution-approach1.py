# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true
# Problem     Group(), Groups() & Groupdict()
# Difficulty  Easy
# Subdomain   Regex and Parsing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-16, 09:30 a.m.
# ──────────────────────────────────────────────────

import re

s = input()
m = re.search(r'([A-Za-z0-9])\1+', s)

if m:
    print(m.group(1))
else:
    print(-1)
