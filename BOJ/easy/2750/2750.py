n = int(input())
lst = [input() for i in range(n)]
result = []

i = 0
while i < n:
    mini = 0
    for j in range(1,n-i):
        if lst[mini] > lst[j]:
            mini = j
    result.append(lst[mini])
    lst.remove(lst[mini])
    i += 1

for i in result:
    if i !=0: print()
    print(i, end="")