# 실패 - 마지막 테스트 통과 못하는 이유?

# 모든 칸을 거쳐서 제자리로 돌아가는 경로가 맞는지 확인

total = 6*6
state = 0 # 잘못된 경로
cnt = 0

alpha = ['A','B','C','D','E','F']
blocks = []
for n1 in alpha:
    for n2 in range(1, 7):
        blocks.append(n1+str(n2))

while cnt < total:
    block = input()
    if block not in blocks:
        #print(block+"중복")
        state = 0
        break
    blocks.remove(block)
    cnt += 1
    #print(cnt)

if len(blocks) == 0:
    state = 1
#else:
    #print(str(blocks)+"남음")
#print(blocks)
if state == 0:
    print("Invalid")
else:
    print("Valid")

