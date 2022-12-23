year, month, day = map(int, input().split())
year2, month2, day2 = map(int, input().split())

# 월 계산
def check_month(m, year):
    result = 0
    day31 = [1,3,5,7,8,10,12]
    if m == 2: # 윤달
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            result += 29
        else :
            result += 28
    elif m in day31:
        result += 31
    else:
        result += 30
    return result

# 년 계산
def check_year(year):
    result = 0
    for i in range(1,13):
        result += check_month(i, year)
    return result

num1 = year*100 + month + 1000*100 + 0.01*day
num2 = year2*100 + month2 + 0.01*day2
#print(num1, num2)

if num1 <=  num2:
    print("gg")
else :
    total = - day
    n_month = range(month,13)
    for i in n_month:
        total += check_month(i, year)

    year += 1
    for j in range(year2 - year):
        total += check_year(year + j)

    for d in range(1,month2):
        total += check_month(d, year2)

    total += day2

    print("D-"+str(total))
