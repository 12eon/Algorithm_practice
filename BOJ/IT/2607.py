# 비슷한 단어

m = int(input())
result = 0
target = list(input().rstrip())

for _ in range(m-1):
    t = target[:]
    v = list(input().rstrip())
    com = sorted(v)

    if com[0] == com[j]: # 같은 구성
        result += 1
    else:
        a, b = com[0], com[j]

        if abs(n[0] - n[j]) == 1: # 추가, 제거
            if n[0] > n[j]:
                b, a = com[0], com[j]
            for i in range(len(b)):
                x = b[:i] + b[i+1:]
                if x == a:
                    result += 1
                    break

        elif abs(n[0] - n[j]) == 0: # 변경
            for i in range(len(b)):
                x = b[:i] + b[i+1:]
                if x in a:
                    result += 1
                    break
print(result)
