# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
# Problem     Find Angle MBC
# Difficulty  Medium
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-15, 08:01 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan(AB / BC))
print(f"{round(angle)}\N{DEGREE SIGN}")
