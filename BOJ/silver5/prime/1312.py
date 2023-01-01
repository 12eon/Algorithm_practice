A, B, N = map(int, input().split())

# 소수점 아래의 숫자가 일의 자리에 위치하도록 조정
r = (A * 10**N) // B
print(r % 10)