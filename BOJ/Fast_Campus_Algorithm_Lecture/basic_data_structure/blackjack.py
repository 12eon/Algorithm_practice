n, m = map(int, input().split())
cards = list(map(int, input().rstrip().split()))
length = len(cards)
result = 0

for x in range(length-2):
    for y in range(x+1, length-1):
        for z in range(y+1,length):
            value = cards[x]+cards[y]+cards[z]
            if value <= m:
                result = max(result, value)
print(result)