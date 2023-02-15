import sys

N = int(sys.stdin.readline())
n_list = sorted([int(sys.stdin.readline()) for i in range(N)])
for x in sorted(n_list):
    print(x)