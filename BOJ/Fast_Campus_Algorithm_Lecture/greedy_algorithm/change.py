price = [500,100,50,10,10,5,1]

money = 1000 - int(input())
n = 0
for p in price:
    n += money//p
    money %= p
print(n)
