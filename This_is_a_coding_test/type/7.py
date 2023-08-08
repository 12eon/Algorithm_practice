# 럭키 스트레이트 https://www.acmicpc.net/problem/18406

n = list(map(int, list(input().rstrip())))
if sum(n[:len(n)//2]) == sum(n[len(n)//2:]):
    print("LUCKY")
else:
    print("READY")