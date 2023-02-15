m,n = input().split()
m = int(m)
n = int(n)

result = []

for i in range(m):
    result.append(list(map(int, list(input().split()))))
for i in range(m):
    cand = list(map(int, list(input().split())))
    for j in range(n):
        result[i][j] += cand[j]
        if i+1 < m or j+1 < n:
            print(result[i][j], end=" ")
        else:
            print(result[i][j])
    if i+1 < m:
        print()