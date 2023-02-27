import sys

q = sys.stdin.readline().rstrip()

i = 0
rod = 0
end = 0
answer = 0
while i < len(q):
    if q[i:i+2] == '()':
        answer += rod
        i += 1
    elif q[i] == '(':
        rod += 1
    elif q[i] == ')':
        rod -= 1
        answer += 1
    i += 1

print(answer)