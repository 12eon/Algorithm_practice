import sys

n = int(sys.stdin.readline())
for _ in range(n):
    p_values = list(sys.stdin.readline().rstrip())
    # 끝에 \n 포함을 주의
    stack = []
    for p in p_values:
        if stack != [] and p == ")" and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(p)
    print(stack)
    if stack != []:
        print("NO")
    else:
        print("YES")