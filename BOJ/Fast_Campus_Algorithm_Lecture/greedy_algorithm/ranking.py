cnt = int(input())
num = []
for _ in range(cnt):
    num += [int(input())]

num.sort()

result = sum([abs(i+1-num[i]) for i in range(cnt)])
print(result)
