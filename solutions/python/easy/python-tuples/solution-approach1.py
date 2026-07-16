# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# Problem     Tuples 
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python
# Status      Accepted
# Submitted   2026-07-16, 09:29 a.m.
# ──────────────────────────────────────────────────

n = int(raw_input())
integer_list = tuple(map(int, raw_input().split()))
print hash(integer_list)
