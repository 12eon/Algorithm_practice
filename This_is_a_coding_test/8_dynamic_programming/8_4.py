# 바닥 공사

n = int(input())
v = [0]*(n+1)

v[1] = 1
v[2] = 3
for i in range(3, n+1):
    v[i] = 2*v[i-2] + v[i-1]
print(v[n] % 796796)