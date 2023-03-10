import sys

i = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))
print(min(values) * max(values))