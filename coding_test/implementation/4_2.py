# 시각

# 도전
'''hour = int(input()) # over개 이상 3의 존재 필요
# 3의 등장 조합
cnt3 = [45,14,1] # 0 1 2

num2 = [3,13,23]+ list(range(30,33)) + list(range(34,40)) + [43,53]
num3 = [33]

x1_cnt = [0]*3
result = [0]*7 # 0개 ~ 6개
for x1 in range(3):
    for x2 in range(3):
        for x3 in range(3):
            if x1_cnt[x1] == 0:
                if x1 == 0:
                     t_cnt = 0
                     for c in range(0,60):
                        if '3' not in str(c) and c <= hour:
                            t_cnt += 1
                     if hour >= 33:
                        t_cnt -= 1
                elif x1 == 1:
                    t_cnt = 0
                    for c in num2:
                        if c <= hour:
                            t_cnt += 1
                else:
                    t_cnt = 0
                    if hour >= 33:
                        t_cnt = 1
                x1_cnt[x1] = t_cnt
            result[x1+x2+x3] += x1_cnt[x1] * cnt3[x2] * cnt3[x3]
print(sum(result[1:]))'''

# 축약
hour = int(input()) # over개 이상 3의 존재 필요

cmp = []
for i in range(3,60):
    if '3' in str(i):
        cmp.append(i)

result = 0
for x in range(60):
    for y in range(60):
        for z in range(60):
            if x <= hour:
                if x not in cmp and y not in cmp and z not in cmp:
                    continue
                result += 1
print(result)