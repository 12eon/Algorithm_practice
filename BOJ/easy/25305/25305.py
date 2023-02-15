N, K = map(int, input().split())
values = sorted(list(map(int, input().split())), reverse=True)
print(values)
print(values[K-1])
