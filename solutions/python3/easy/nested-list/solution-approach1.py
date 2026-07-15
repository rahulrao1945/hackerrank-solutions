# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Problem     Nested Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-15, 07:52 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted(set(score for name, score in students))
    second_lowest = scores[1]

    names = sorted(name for name, score in students if score == second_lowest)

    for name in names:
        print(name)
