# 왕실의 나이트

input_v = list(input())
cnt = 8 # 8x8 지정됨

# alpha = [chr(i) for i in range(97,104)] 문자끼리 비교
num = list(range(1,9))

x = [num.index(int(input_v[1])), num.index(int(ord(input_v[0])) - int(ord('a')) +1)]
cmp = [[1,2],[-1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,1],[-2,-1]]

# 이동 문제에서는 중간 값 저장하는 dx, dy 자주 사용
result = 0
for c in cmp:
    dx = x[0] + c[0]
    dy = x[1] + c[1]
    if dx < 0 or dx >= cnt or dy < 0 or dy >= cnt:
        continue
    result += 1
print(result)