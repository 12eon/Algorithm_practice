import sys

cnt = int(sys.stdin.readline())

count = 0
result = []
stack = []
for _ in range(cnt):
    data = int(sys.stdin.readline())
    while count < data:
        stack.append(count+1)
        result.append('+')
        count += 1
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)
print('\n'.join(result))

# 다음이 현재보다 바로 아래 나올 수 아니면 실패
# = 자기뒤 수list 중 자기보다 큰 수x
# = stack에서 될 수 있는 가장 큰 수가 자기여야함