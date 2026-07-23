# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true
# Problem     Text Alignment
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-23, 11:23 p.m.
# ──────────────────────────────────────────────────

thickness = int(input())
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * (2 * i + 1)).center(thickness * 2 - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print((c * (2 * (thickness - i) - 1)).center(thickness * 2 - 1).rjust(thickness * 6 - 1))
