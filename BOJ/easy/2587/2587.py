nums = 0
n_list = []
for i in range(5):
    value = int(input())
    n_list.append(value)
    nums += value
print(nums//5)
print(sorted(n_list)[2])