# 막대기
goal = int(input())

sticks = [64]
# 기준으로 이용
stick = 64 # 1 <= goal <= 64

count = 0
while stick > goal:
      count += 1
      pick = min(sticks)
      sticks.remove(pick)
      pick //= 2
      sticks.append(pick)
      if sum(sticks) < goal:
            sticks.append(pick)
      stick = sum(sticks)

print(len(sticks))