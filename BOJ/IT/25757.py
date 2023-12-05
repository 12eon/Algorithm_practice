# 임스와 함께하는 미니게임 : 중복 없게

n, type = input().split()

m = 3
if type == 'Y': m = 1
elif type == 'F': m = 2

n = int(n)
p = set([input() for _ in range(n)])
print(len(p)//m)
