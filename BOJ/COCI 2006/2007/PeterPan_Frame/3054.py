# 3의 배수 = 웬디 프레임 / 나머지  = 피터팬 프레임

a_list = list(input())
length = len(a_list)

result = []


def make_frame(alpha, type):
    result = [['.' for x in range(5)] for y in range(5)]
    result[2][2] = alpha
    mark = '#'

    if type == 'p':
        mark = '*'

    row = 0
    std = 0

    for i in range(3):
        result[2-i][i] = mark
        result[2-i][4-i] = mark

    for i in range(2):
        result[3+i][i+1] = mark
        result[3+i][3-i] = mark

    return result


def add_list(result, answer, pre):
    if result == []:
        result = answer
    else:
        for i in range(5):
            result[i] += answer[i][1:]
    if pre == 1:
        result[2][-5] = '*'
    return result


def printer(result):
    for i in range(5):
        print(''.join(result[i]))

if length < 1:
    printer(make_frame(a_list[0], 'w'))
else:
    for i in range(length):
        if i%3 != 2:
            pre = 0
            result = add_list(result, make_frame(a_list[i], 'w'), pre)
        else:
            pre = 1  # * 처리 완료
            result = add_list(result, make_frame(a_list[i], 'p'), pre)

printer(result)