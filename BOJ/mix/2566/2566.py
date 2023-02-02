result = 0
value = [1,1]

for i in range(9):
    lst = list(map(int, input().split()))
    cmp = max(lst)
    if cmp >= result:
        result = cmp
        value[0] = i+1
        value[1] = lst.index(cmp)+1
    print(value, result)

print(result, end =" ")
print()
print(value[0], end=" ")
print(value[1], end="")