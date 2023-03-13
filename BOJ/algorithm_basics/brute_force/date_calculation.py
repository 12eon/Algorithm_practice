import sys

n = list(map(int, sys.stdin.readline().split()))
std = [15,28,19]
result = 0

if n[0] == n[1] and n[1] == n[2]:
    print(n[0])
else:
    goal = 1
    while True:
        if (goal-n[0])%15 == 0 and (goal-n[1])%28 == 0 and (goal-n[2])%19 == 0:
            break
        goal += 1
    print(goal)