import sys

class Deque:
    def __init__(self):
        self.d = []

    def push_front(self, x):
        self.d.insert(0,x)

    def push_back(self, x):
        self.d.append(x)

    def pop_front(self):
        if self.size() > 0:
            return self.d.pop(0)
        return -1

    def pop_back(self):
        if self.size() > 0:
            return self.d.pop()
        return -1

    def size(self):
        return len(self.d)

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def front(self):
        if self.size() > 0:
            return self.d[0]
        return -1

    def back(self):
        if self.size() > 0:
            return self.d[-1]
        return -1

deque = Deque()
n = int(sys.stdin.readline())
for _ in range(n):
    v = list(sys.stdin.readline().rstrip().split())
    if "push" in v[0]:
        if v[0] == "push_front":
            deque.push_front(int(v[1]))
        if v[0] == "push_back":
            deque.push_back(int(v[1]))
    elif "pop" in v[0]:
        if v[0] == "pop_front":
            print(deque.pop_front())
        if v[0] == "pop_back":
            print(deque.pop_back())
    elif v[0] == "size":
        print(deque.size())
    elif v[0] == "empty":
        print(deque.empty())
    elif v[0] == "front":
        print(deque.front())
    elif v[0] == "back":
        print(deque.back())
