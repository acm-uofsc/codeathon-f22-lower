n = int(input())

counter = 0
for _ in range(n):
    line = input()
    counter += line.count('Romeo')

print(counter)
