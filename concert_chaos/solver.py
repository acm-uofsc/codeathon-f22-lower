#   1
#   2*(1) + 1
#   2*(2) + 1
#   2*(3) + 1
#   y = 2*x + 1

# The items in the array should be sorted left to right, top to bottom.


class Solver:
    def __init__(self, input_array):
        self.input_array = input_array
        self.size = len(input_array)
        self.val = 52
        self.nums_arr = [0] + [2*x + 1 for x in range((self.val))]

    def line_changer_v2(self, arr, val, index):
        for i in range(index+1):
            arr[i][index] = val
            arr[index][i] = val
        return arr

    def sum(self, nums_arr, sum_value):
        cont = {}
        for n, i in enumerate(nums_arr):
            if sum_value - nums_arr[n] in cont:
                return [cont[sum_value - nums_arr[n]], n]
            else:
                cont[nums_arr[n]] = n

    def main(self):
        d = {}
        for i in self.input_array:
            for j in i:
                if j in d:
                    d[j] = d[j] + 1
                else:
                    d[j] = 1
        arr = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for key, value in d.items():
            v = self.sum(self.nums_arr, value)
            if v[0] != 0:
                arr = self.line_changer_v2(arr, key, v[0]-1)
            arr = self.line_changer_v2(arr, key, v[1]-1)

        return arr


if __name__ == "__main__":
    input_array = [['C', 'C', 'C', 'D', 'D'],
                   ['B', 'B', 'C', 'D', 'D'],
                   ['D', 'D', 'D', 'D', 'D'],
                   ['D', 'D', 'D', 'D', 'D'],
                   ['A', 'B', 'C', 'D', 'D']]
    solve = Solver(input_array)
    arr = solve.main()
    for j in arr:
        for i in j:
            print(i, end=' ')
        print()
