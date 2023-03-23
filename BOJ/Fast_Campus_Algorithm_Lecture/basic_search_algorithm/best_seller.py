cnt = int(input())
name = {}
m = 1
cmp = []
for _ in range(cnt):
    n = input().rstrip()
    if n not in name:
        name[n] = 1
    else:
        name[n] += 1

result = []
m = max(name.values())
for k, v in name.items():
    print(k,v)
    if v == m:
        result.append(k)
print(sorted(result)[0])