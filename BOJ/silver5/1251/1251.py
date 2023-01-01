word = list(input())

length = len(word)
result = "z"*50

# 선택된 인덱스의 앞에서 자르는 경우로, 2개(i,j) 선택
for i in range(1, length-1):
    for j in range(i+1,length):
        part = ''
        part = part.join(word[i-1::-1] + word[j-1:i-1:-1] + word[:j-1:-1])
        if result > part:
            result = part

print(result)
