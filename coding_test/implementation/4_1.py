# 상하좌우

cnt = int(input())
path = list(input().split())
st = ['U','D','L','R']
value = [1, 1]

# 한번에 초과여부 확인 + 후보값 저장
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for p in path:
    i = st.index(p)
    xcnd = value[0] + dx[i]
    ycnd = value[1] + dy[i]
    #print(i, xcnd, ycnd)
    if xcnd < 1 or xcnd > cnt or ycnd < 1 or ycnd > cnt:
        continue
    value = [xcnd, ycnd]
print(value[0], value[1])

# 실패 이유 : 너무 조건 검사가 많음
'''
for p in path:
    if p == st[0] and value[1] > 1: # 조건 확인
        value[1] -= 1
    elif p == st[1] and value[1] < cnt:
        value[1] += 1
    elif p == st[2] and value[0] > 1:
        value[0] -= 1
    elif p == st[3] and value[0] < cnt:
       value[0] += 1
print(value[0], value[1])'''
