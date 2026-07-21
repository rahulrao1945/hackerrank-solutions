# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
# Problem     Capitalize!
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-21, 10:36 p.m.
# ──────────────────────────────────────────────────



# Complete the solve function below.
import os

def solve(s):
    words = s.split(" ")
    result = []

    for word in words:
        if len(word) > 0 and word[0].isalpha():
            result.append(word[0].upper() + word[1:])
        else:
            result.append(word)

    return " ".join(result)

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

