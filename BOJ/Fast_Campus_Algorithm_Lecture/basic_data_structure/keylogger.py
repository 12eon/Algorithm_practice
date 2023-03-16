cnt = int(input())

for _ in range(cnt):
    stack = [] # 뒤 : open
    stack2 = [] # 뒤 : open
    keys = [x for x in input().rstrip()]
    for k in keys:
        if k == '<':
            if len(stack) > 0:
                stack2.append(stack.pop())
        elif k == '>':
            if len(stack2) > 0:
                stack.append(stack2.pop())
        elif k == '-':
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(k)
    stack2.reverse()
    print(''.join(stack+stack2))