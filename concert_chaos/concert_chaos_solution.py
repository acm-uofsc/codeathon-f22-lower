size = int(input())
input_array = [list(map(str, input().split())) for _ in range(size)]

val = 52
nums_arr = [0] + [2*x + 1 for x in range((val))]

d = {}

for i in input_array:
    for j in i:
        if j in d:
            d[j] = d[j] + 1
        else:
            d[j] = 1


arr = [[0 for _ in range(size)] for _ in range(size)]


def line_changer_v2(arr, val, index):
    for i in range(index+1):
        arr[i][index] = val
        arr[index][i] = val
    return arr


def sum(nums_arr, sum_value):
    cont = {}
    for n, i in enumerate(nums_arr):
        if sum_value - nums_arr[n] in cont:
            return [cont[sum_value - nums_arr[n]], n]
        else:
            cont[nums_arr[n]] = n


for key, value in d.items():
    v = sum(nums_arr, value)
    if v[0] != 0:
        arr = line_changer_v2(arr, key, v[0]-1)
    arr = line_changer_v2(arr, key, v[1]-1)

for j in arr:
    for i in j:
        print(i, end=' ')
    print()
