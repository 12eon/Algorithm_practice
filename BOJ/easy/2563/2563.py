points = [[0 for i in range(100)] for j in range(100)]

#def printer(lst):
#    for i in range(len(lst)):
#        print(lst[i])

n = 0
cnt = int(input())
for z in range(cnt):
    x, y = map(int, input().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            if points[i][j] == 0:
                points[i][j] = 1
                n += 1

print(n)