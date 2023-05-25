# 모험가 길드 : 공포도가 높은 사람끼리 모으기

n = list(map(int, input().split(''))
print(n)
now = n[0]

for i in range(1,n):
    if now <= 1 or n[i] <= 1:
        now += n[i]
    else:
        now *= n[i]
print(now)
