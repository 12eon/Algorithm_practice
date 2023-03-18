n = int(input())

def fibonacci(n):
    num = [0,1]
    for _ in range(2,n+1):
        num.append(num[-2]+num[-1])
    return num[-1]

print(fibonacci(n))