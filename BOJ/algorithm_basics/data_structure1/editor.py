# 시간초과 : insert와 pop에 의해
# 해결 : stack 2개로 append와 pop만 이용하도록
import sys

stack = list(sys.stdin.readline().rstrip())
stack2 = list()

n = int(sys.stdin.readline())
for _ in range(n):
    value = sys.stdin.readline().rstrip()
    if value == 'L':
        if stack != []:
            stack2.append(stack.pop())
    elif value == 'D': #?
        if stack2 != []:
            stack.append(stack2.pop())
    elif value == 'B':
        if stack != []:
            stack.pop()
    elif value[0] == "P":
        stack.append(value[-1])
    print(stack, stack2)

print(''.join(stack), end='')
print(''.join(reversed(stack2)))
