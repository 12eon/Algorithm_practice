import sys

n = list(map(int, sys.stdin.readline().split()))
goal = 1
while True:
    if (goal-n[0])%15 == 0 and (goal-n[1])%28 == 0 and (goal-n[2])%19 == 0:
        break
    goal += 1
print(goal)