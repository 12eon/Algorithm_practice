# 큰 수의 법칙

n,m,k = map(int, input().split())
num = list(map(int, input().split()))

num1 = max(num)
num2 = 0
for v in num:
    if v > num2 and v != num1:
        num2 = v

# 반복 단위
value = num1*k + num2
v_cnt = k+1

print((m//v_cnt)*value + (m%v_cnt)*num1)