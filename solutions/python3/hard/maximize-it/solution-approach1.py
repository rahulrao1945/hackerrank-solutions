# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
# Problem     Maximize It!
# Difficulty  Hard
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-15, 07:53 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    k, m = map(int, input().split())
    lists = []

    for _ in range(k):
        data = list(map(int, input().split()))
        lists.append(data[1:])

    result = max(sum(x * x for x in p) % m for p in product(*lists))
    print(result)
