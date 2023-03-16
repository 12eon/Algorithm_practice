import sys

ascend = 1
descend = 1
scale = list(map(int, input().rstrip().split()))

for i in range(7):
    if scale[i] > scale[i+1]:
        ascend = 0
    else:
        descend = 0

if ascend == 1:
    print("ascending")
elif descend == 1:
    print("descending")
else:
    print("mixed")