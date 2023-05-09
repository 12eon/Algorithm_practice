# 떡볶이 떡 만들기

n,m = map(int, input().split())
rice = list(map(int, input().split()))
rice.sort()

cmp = 0
start = 0
end = rice[-1]
while (start <= end):
    mid = (start+end)//2
    rest = 0

    for i in rice:
        if mid < i:
            rest += (i-mid)
    if m <= rest:
        cmp = max(cmp, mid)
        start = mid +1
    else:
        end = mid+1
print(cmp)