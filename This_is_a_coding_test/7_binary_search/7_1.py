# 부품 찾기

n = int(input())
n_part = list(map(int, input().split()))


m = int(input())
m_part = list(map(int, input().split()))

# 1) set 자료형 이용 : in 확인

# 2) 이진 탐색
"""
def binarySearch(a, target, start, end):
	if end < start: # 엇갈림 : target 없음
		return None
	mid = (start+end)//2
	if a[mid] == target:
		return mid
	if a[mid] > target:
		return binarySearch(a, target, start, mid-1)
	else:
		return binarySearch(a, target, mid+1, end)

n_part.sort()

for i in m_part:
    result = binarySearch(n_part, i, 0, n-1)
    if result == None:
        print('no')
    else:
        print('yes')
"""
# 3) 계수 정렬
v = [0]*(max(m) + 1)
for j in n_part:
    v[j] += 1

for i in m_part:
    if v[i] == 0:
        print('no')
    else:
        print('yes')