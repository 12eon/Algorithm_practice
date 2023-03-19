n,r,c = map(int, input().split())

result = 0
length = 2**n//2
mid = [2**n//2, 2**n//2]
for _ in range(n):
    if r < mid[0]:
        if c < mid[1]:
            part = 0
            mid[1] -= length//2
        else:
            part = 1
            mid[1] += length//2
        mid[0] -= length//2
    else:
        if c < mid[1]:
            part = 2
            mid[1] -= length//2
        else:
            part = 3
            mid[1] += length//2
        mid[0] += length//2
    result += part*length*length
    length //= 2
print(result)