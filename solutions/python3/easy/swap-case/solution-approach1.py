# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
# Problem     sWAP cASE
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-17, 08:08 a.m.
# ──────────────────────────────────────────────────

def swap_case(s):
    result = ""
    for ch in s:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch
    return result

