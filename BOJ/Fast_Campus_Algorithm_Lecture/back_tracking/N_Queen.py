
def check(x):
    for i in range(x): # 전에 높은 것
        if row[x] == row[i]:# 위쪽
            return False
        if abs(row[x] - row[i]) == x - i: #대각선
            return False
    return True

# x번째 행에 대하여 처리
def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1) # 다음행

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)