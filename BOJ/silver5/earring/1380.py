cnt = 1

while 1:
    name = []
    value = int(input())
    if value == 0:
        break

    for i in range(value):
        name += [input()]

    num = [0]*value
    for i in range(2*value-1):
        n, a = input().split()
        num[int(n)-1] += 1
    #print(num)
    #print(name)

    for i in range(len(name)):
        if num[i] == 1:
            print(str(cnt) + " " + str(name[i]))
            cnt += 1
