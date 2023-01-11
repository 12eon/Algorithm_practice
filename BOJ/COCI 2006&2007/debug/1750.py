# 실패

def square_killer(l, num, values):
    m2, n2 = num[0], num[1]
    for i in range(m2, l+m2):
        for j in range(n2, l+n2):
            if values[i][j] != values[l-i-1][l-j-1]:
                return 0 # false
    return l #true


result = 1
m, n = map(int, input().split())
length = min(m,n)

values = []
for i in range(m):
    values += [[int(x) for x in list(input())]]


def check(length, m, n, values):
    while length > 1:
        i = 0
        while i < m-length+1 :
            j = 0
            while j < n-length+1 :
                candidate = square_killer(length, [i,j], values)
                if candidate > 0:
                    return candidate
                j += 1
            i += 1
        length -= 1

    return 1

result = check(length, m, n, values)
print(result)