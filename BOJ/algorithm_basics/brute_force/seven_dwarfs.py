import sys
values = []
for _ in range(9):
    values.append(int(sys.stdin.readline()))
result = sum(values)
values.sort()

def calc(values):
    for i in range(0,8):
        for j in range(i+1, 9):
            if result - values[i] - values[j] == 100:
                return [i,j]

i,j = calc(values)
for n in range(9):
    if n != i and n!= j:
        print(values[n])