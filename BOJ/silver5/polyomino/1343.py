n = input()

box = [len(x) for x in list(n.split('.'))]
length = len(box)
values = []

# A는 4칸, B는 2칸으로 조합이 지정됨
cnt = 0
value = ""
while cnt < length:
    if box[cnt] >= 4:
        value += (box[cnt] // 4) * 'AAAA'
        box[cnt] %= 4
    elif box[cnt] >= 2:
        value += (box[cnt] // 2) * 'BB'
        box[cnt] %= 2

    if box[cnt] == 0:
        cnt += 1
        values += [value]
        value = ""
    elif box[cnt] == 1:
        break

if cnt < length:
    print(-1)
else:
    cmp = list(''.join(values))
    result = ""

    i = 0
    for x in list(n):
        if x == '.':
            result += '.'
        else:
            result += cmp[i]
            i += 1
    print(result)