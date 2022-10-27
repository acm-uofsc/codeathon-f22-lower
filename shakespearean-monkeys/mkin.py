import random
import string

MIN_LINES = 5
MAX_LINES = 100

MIN_LLEN = 1000
MAX_LLEN = 10000

MIN_SEARCH_LEN = 10
MAX_SEARCH_LEN = 100


sample_id = int(input())
if sample_id == 0:
    num_lines = 10
    line_len = 75
    search_key = 'O Romeo, Romeo, wherefore art thou Romeo?'
else:
    num_lines = random.randint(MIN_LINES, MAX_LINES)
    line_len = random.randint(MIN_LLEN, MAX_LLEN)
    search_key_len = random.randint(MIN_SEARCH_LEN, MAX_SEARCH_LEN)
    L1 = random.choice(string.ascii_letters)
    non_l1 = list(string.ascii_letters)
    non_l1.remove(L1)
    L2 = random.choice(non_l1)
    search_key = ''.join(
        [L1] * (search_key_len // 2) + [L2] * (search_key_len // 2))


print(num_lines)
print(search_key)
for _ in range(num_lines):
    search_insert_loc = random.randint(0, line_len - (len(search_key) // 2))
    j = 0
    while j < line_len:
        if search_insert_loc < line_len - len(search_key) and \
                j == search_insert_loc:
            print(search_key, end='')
            j += len(search_key)
        else:
            choice = random.choice(string.ascii_letters)
            print(choice, end='')
            j += 1
    print()
