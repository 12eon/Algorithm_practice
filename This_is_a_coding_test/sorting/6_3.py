# 두 배열의 원소 교체

n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break
print(sum(a))

"""
c = 0
while c<k :
    i = a.index(min(a))
    j = b.index(max(b))
    if a[i] < b[j]:
        c += 1
        a[i], b[j] = b[j], a[i]
    else:
        break
"""