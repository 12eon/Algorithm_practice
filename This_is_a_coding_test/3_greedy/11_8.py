# 문자열 재정렬

st = list(input())
st.sort()
print(st)
start = len(st)
for i in range(len(st)):
    if ord('A') <= ord(st[i]) <= ord('Z'):
        start = i
        break
    else:
        st[i] = int(st[i])
print(''.join(st[start:]) + str(sum(st[:start])))
