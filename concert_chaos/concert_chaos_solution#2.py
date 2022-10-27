from collections import Counter

n = int(input())

chars = []
for _ in range(n):
    chars += input().split(' ')

count = Counter(chars)

even = []
for elem, amnt in count.items():
    if amnt % 2 == 0:
        count[elem] = amnt / 2 - 1
        even.append(elem)

reverse_count = count.most_common()
reverse_count.reverse()

# DEFINE OUTPUT MATRIX
arr = [[0 for _ in range(n)] for _ in range(n)]


def line_changer_v2(arr, val, index):
    for i in range(index + 1):
        arr[i][index] = val
        arr[index][i] = val
    return arr


i = 0
num_even = 0
while i < n:
    elem = reverse_count[i - num_even][0]
    arr = line_changer_v2(arr, elem, i)
    if elem in even:
        num_even += 1
        i += 1
        arr = line_changer_v2(arr, elem, i)
    i += 1

for row in arr:
    print(*row, sep=' ')