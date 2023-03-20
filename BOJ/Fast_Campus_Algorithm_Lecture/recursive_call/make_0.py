import copy

def recursive(array, n):
    if len(array) == n:
        calc.append(copy.deepcopy(array))
        return
    array += ' '
    recursive(array,n)
    array.pop()

    array += '+'
    recursive(array,n)
    array.pop()

    array += '-'
    recursive(array,n)
    array.pop()

test = int(input())
for _ in range(test):
    calc = []
    n = int(input())
    recursive([], n-1)

    integer = [i for i in range(1,n+1)]

    for c in calc:
        s = ''
        for i in range(n-1):
            s += str(i+1)+c[i]
        s += str(integer[-1])
        if eval(s.replace(" ","")) == 0:
            print(s)
    print()