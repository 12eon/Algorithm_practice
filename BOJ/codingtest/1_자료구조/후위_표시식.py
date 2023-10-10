expression = list(input().rstrip())
op = {"+": 1, "-": 1, "*": 2, "/": 2}
res = ""
s = []

for exp in expression:
    if exp.isalpha():
        res += exp
    elif exp == "(":
        s.append(exp)
    elif exp == ")":
        while s[-1] != "(":
            res += s.pop()
        s.pop()
    elif exp in op: # 연산자 경우
        while s and s[-1] != "(" and (op[exp] <= op[s[-1]]): # 들어올 연산자가 이전보다 우선 순위가 낮음
            res += s.pop()
        s.append(exp)
    print(res, s)
while s:
    res += s.pop()
print(res)