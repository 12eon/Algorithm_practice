import hashlib

st = input().rstrip())
hash = hashlib.sha256()
hash.update(st.encode())
print(hash.hexdigest())