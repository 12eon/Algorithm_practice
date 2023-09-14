s1 = list(input())
s2 = list(input())

g = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

for i in range(1, len(s1)+1):
    g[0][i] = i

for i in range(1, len(s2)+1):
    g[i][0] = i

for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s2[i-1] == s1[j-1]:
            g[i][j] = g[i-1][j-1]
        else:
            g[i][j] = min(g[i-1][j-1], g[i][j-1], g[i-1][j]) + 1

# for i in range(len(s2)+1):
#     print(g[i])
print(g[len(s2)][len(s1)])

##########
# edit add
# delete (i)

# 동일하면 edit 위치의 내용을 그래로 가져오기