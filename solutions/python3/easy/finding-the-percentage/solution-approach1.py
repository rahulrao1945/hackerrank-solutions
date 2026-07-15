# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
# Problem     Finding the percentage
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-15, 07:52 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        data = input().split()
        name = data[0]
        marks = list(map(float, data[1:]))
        student_marks[name] = marks

    query_name = input()

    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")
