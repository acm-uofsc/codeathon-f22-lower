n = int(input())
search_key = input()

counter = 0
for _ in range(n):
    line = input()
    counter += line.count(search_key)

print(counter)
