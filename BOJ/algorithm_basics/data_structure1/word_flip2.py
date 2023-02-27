# 특정 조건 -> while
import sys

string = list(sys.stdin.readline().rstrip())

answer = []
word = []
i = 0
while i < len(string):
    if string[i] == '<':
        end = string[i:].index('>')
        answer.append(''.join(string[i:i+end+1]))
        i += end+1
    elif string[i] == ' ':
        answer.append(' ')
        i += 1
    else:
        while i < len(string):
            if string[i] == '<' or string[i] == ' ' :
                break
            word.append(string[i])
            i += 1
        answer.append(''.join(reversed(word)))
        word = []

print(''.join(answer))