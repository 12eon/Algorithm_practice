# https://school.programmers.co.kr/learn/courses/30/lessons/12952

import sys
import math

def check_next(i, n, v):
    if (i == n):
        #print(v)
        return (1)
    count = 0
    for x in range(0, n): # (i, x)
        state = 1
        if x not in v: # 속도 향상
            for x2 in range(0, i):
                if x == v[x2] or abs(x2-i) == abs(v[x2]-x):
                    state = 0
                    break
            if state == 1:
                v[i] = x
                count += check_next(i+1, n, v)
                v[i] = -1

    return count

def solution(n):
    v = [-1 for _ in range(n)]
    return check_next(0, n, v)