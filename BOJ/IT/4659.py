# 비밀번호 발음하기

while True:
    pw = input().rstrip()
    if pw == "end":
        break

    # 조건 체크
    clist = ['a','e','i','o','u']

    cnt = 0
    for c in clist:
        if c in pw:
            cnt = 1
            break
    if cnt == 0:
        print("<"+str(pw)+"> is not acceptable.")
        continue

    is_acceptable = True # 둘중에 하나만 출력해야하는 경우

    for i in range(len(pw) - 2):
        check = []
        for j in range(i, i + 3):
            check += [pw[j] in clist]
        s = sum(check)
        if s == 0 or s == 3:
            is_acceptable = False
            break
        if pw[i] == pw[i + 1] and pw[i] not in ['e', 'o']:
            is_acceptable = False
            break

    if len(pw) > 1 and pw[-1] == pw[-2] and pw[-1] not in ['e', 'o']:
        is_acceptable = False

    # 두번 출력 없게 처리
    if is_acceptable:
        print("<" + pw + "> is acceptable.")
    else:
        print("<" + pw + "> is not acceptable.")
