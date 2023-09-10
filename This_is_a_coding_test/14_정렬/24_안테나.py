n = int(input())
hs = sorted(list(map(int, input().split())))
print(hs[(len(hs)-1)//2]) # 평균이 아닌 중앙값