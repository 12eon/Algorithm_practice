import math

day = int(input())
sch = []
v = [0 for _ in range(day+1)] # last day check

for i in range(day):
    sch.append(list(map(int, input().split())))

for i in range(day-1,-1,-1): # work
    if i + sch[i][0] <= day: # over
        v[i] = max(v[i+1], v[i + sch[i][0]] + sch[i][1])
    else:
        v[i] = v[i+1]

print(v[0])