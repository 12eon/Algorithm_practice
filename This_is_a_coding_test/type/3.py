# 문자열 뒤집기

n = list(input().rstrip())
num = list(map(int, n))


count0 = 0
count1 = 0

if num[0] == 1:
    count0 += 1
else:
    count1 += 1

for i in range(len(num) - 1):
    if num[i] != num[i + 1]:
        if num[i + 1] == 1:
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))