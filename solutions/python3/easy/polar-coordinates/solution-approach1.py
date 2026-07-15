# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
# Problem     Polar Coordinates
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-15, 08:00 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

z = complex(input())

print(abs(z))
print(cmath.phase(z))
