total = list(input().rstrip())
word = list(input().rstrip())
result = 0
j = 0

while j <= len(total) - len(word) :
    if total[j:j+len(word)] == word:
        result += 1
        j += len(word)
    else:
        j += 1
print(result)