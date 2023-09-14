# 문자열 압축 : https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    if len(s) == 1: # 시간 초과 방지
        return 1
    result=[]
    for i in range(1, (len(s)//2)+1):
        b = ''
        cnt = 1
        tmp=s[:i]

        for j in range(i, len(s), i): # 비교 대상
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1: # 이전 반복
                    b = b + str(cnt)+tmp
                else: # 반복 없음
                    b = b + tmp
                tmp=s[j:j+i] # 초과되는 부분은 알아서 안 포함
                cnt = 1
        if cnt!=1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp

        result.append(len(b))
    return min(result)