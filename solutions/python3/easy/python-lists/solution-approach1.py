# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-16, 09:23 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        cmd = input().split()

        if cmd[0] == "insert":
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "print":
            print(lst)
        elif cmd[0] == "remove":
            lst.remove(int(cmd[1]))
        elif cmd[0] == "append":
            lst.append(int(cmd[1]))
        elif cmd[0] == "sort":
            lst.sort()
        elif cmd[0] == "pop":
            lst.pop()
        elif cmd[0] == "reverse":
            lst.reverse()
