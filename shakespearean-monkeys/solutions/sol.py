num_lines, num_keys = list(map(int, input().split()))
search_line = input()
if ';' in search_line:
    search_keys = search_line.split(';')
else:
    search_keys = [search_line]
assert len(search_keys) == num_keys, print(search_keys)


for _ in range(num_lines):
    line = input()
    counters = []
    for search_key in search_keys:
        counter = line.count(search_key)
        counters.append(counter)
    print(*counters)
