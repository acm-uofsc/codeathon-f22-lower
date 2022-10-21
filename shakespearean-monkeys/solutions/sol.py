n = int(input())
search_key = input()

for _ in range(n):
    line = input()
    counter = line.count(search_key)
    print(counter)
