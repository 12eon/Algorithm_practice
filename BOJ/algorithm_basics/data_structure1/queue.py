class Queue:
    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        if self.size() > 0:
            return self.q.pop(0)
        return -1

    def size(self):
        return len(self.q)

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def front(self):
        if self.size() > 0:
            return self.q[0]
        return -1

    def back(self):
        if self.size() > 0:
            return self.q[-1]
        return -1

import sys
q = Queue()

cnt = int(sys.stdin.readline())
for _ in range(cnt):
    value = sys.stdin.readline().rstrip()
    if "push" in value:
        q.push(int(list(value.split())[1]))
    elif value == "pop":
        print(q.pop())
    elif value == "size":
        print(q.size())
    elif value == "empty":
        print(q.empty())
    elif value == "front":
        print(q.front())
    elif value == "back":
        print(q.back())
