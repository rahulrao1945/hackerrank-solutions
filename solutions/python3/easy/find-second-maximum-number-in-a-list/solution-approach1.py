# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-15, 07:51 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(sorted(set(arr))[-2])
