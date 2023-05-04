import sys

d_cnt, q_cnt = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))
plus_data = [0]

# solve
plus = 0
for d in data:
    plus += d
    plus_data.append(plus)
#print(plus_data)

for _ in range(q_cnt):
    start, end = map(int, sys.stdin.readline().split())
    print(plus_data[end] - plus_data[start-1])
