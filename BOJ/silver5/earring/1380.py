# 실패

cnt = 1

n = [] # input
std = [] # [시작 인덱스, 끝 인덱스]

while 1:
    value = input()
    if value == '0':
        break
    n.append(value)

    if len(value) < 3:
        if len(std) == 0:
            std += [[0]]
        else:
            pre = std[-1][-1]
            std[-1] += [pre + len(n) - 2]
            std += [[pre + len(n) - 1]]
std[-1] += [len(n)-1]
#print(std)

s = 0
while s < len(std) :
    p = int(n[std[s][0]])
    name = n[std[s][0]+1:std[s][0]+p+1]
    index = std[s][0]+p+1

    cmp = []
    for i in range(std[s][1]-index+1):
        num = list(n[index+i])[0]
        if num not in cmp:
            cmp.append(num)
        else:
            cmp.remove(num)

    for i in range(len(cmp)):
        print(str(cnt) + " " + str(name[i]))
        cnt += 1

    s += 1
