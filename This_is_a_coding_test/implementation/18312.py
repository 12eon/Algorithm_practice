# 시각
hour, k = input().split() # k==0 가능하므로, 0인 문자도 고려

result = 0
for x in range(int(hour)+1):
    for y in range(60):
        for z in range(60):
            cmp = ''
            if x < 10:
                cmp += '0'
            cmp +=str(x)
            if y < 10:
                cmp += '0'
            cmp +=str(y)
            if z < 10:
                cmp += '0'
            cmp += str(z)
            if k in cmp:
                result += 1
print(result)