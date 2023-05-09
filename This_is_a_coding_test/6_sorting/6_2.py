# 성적이 낮은 순서로 학생 출력하기

n = int(input())
v = []
for _ in range(n):
    m,n = map(int, input().split())
    n = int(n)
    v.append((n,m))

v.sort(key = lambda x: x[0])

for x in v:
    print(x[1])
