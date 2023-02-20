import sys

# 정수 저장하는 스택
class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        if self.size() > 0:
            return self.s.pop(-1)
        return -1

    def size(self):
        return len(self.s)

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def top(self):
        if self.size() > 0:
            return self.s[-1]
        return -1


stack = Stack()

n = int(sys.stdin.readline())
for _ in range(n):
    v = sys.stdin.readline().rstrip()
    if "push" in v:
        v2 = int(v.split()[1])
        stack.push(v2)
    elif v == "top":
        print(stack.top())
    elif v == "size":
        print(stack.size())
    elif v == "empty":
        print(stack.empty())
    elif v == "pop":
        print(stack.pop())
