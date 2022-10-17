import random
import string

MIN_LINES = 5
MAX_LINES = 100

MIN_LLEN = 1000
MAX_LLEN = 10000

MIN_SEARCH_LEN = 5
MAX_SEARCH_LEN = 100

MIN_SEARCH_TERMS = 1
MAX_SEARCH_TERMS = 100


sample_id = int(input())
if sample_id == 0:
    num_lines = 10
    line_len = 75
    num_terms = 1
    search_occurance = 0.1
    search_keys = ['O Romeo, Romeo, wherefore art thou Romeo?']
    print(num_lines, num_terms)
    print(*search_keys, sep=';')
    print('DhbgjdsGKdAdFogOQlpeNhpRXINoktUNtvYZmiziQkWYpyvCcGcxqIWIITluYYiUOxaxvzkMEJu\nxSpKwMjbmZNcvZufxMnzHOywiXtRmdXjcOQALzrpOBOWGnAmOSnRQujRkGCOLXZdgxzncAWQIYp\nVhjnihlPdweENvfRPYhuAeEvUzuHpueLtZTvfoYedjTjPZNgnryFDmtfttoViVOsJhVRgrPTVoY\nYeFHcUlVAGCJRXlFGxwxGVcgCWTJVJwuVNzcNWiMHPudyTpucFGPIlsoYLUJDHvGvbknzqrGiFV\nnrhdsRScrhILObTdVrCjhdJHtGPwpkTXaOqsLWiAuqdJXZTqRnMJTPWRybMuBmsftWPhHdqXgKe\nEUCLBngENblmOFKAODpfmfhnzYWoQQLO Romeo, Romeo, wherefore art thou Romeo?isE\nSqKtYUCPGVGxNWATnuBKmUzdfiBuKuuHUmSvpcFhfNchDAHyfSRJJOYdzPdcqRicEkOYxbhZldV\ngdLYApCJifqSwHQVEiNgjXThrykECSXohtiHGeWFgdcNwLWcIJmsFixZjbnFdKpuPmbRtKHVcwi\nccywTeRuICMuPJBVYrEbLIZEjzvlCzHuwvfUAPunlOaoqVxwretoXkgspahqWKJmVXPXRDizutK\nGGbervQfmUfQoxeoJSyWPLxcdYtbyUNfFNoWdxaSdzUDKHOoUAuvEJnvRWeODHupDNeMJriQxra')
    exit()
else:
    num_lines = random.randint(MIN_LINES, MAX_LINES)
    line_len = random.randint(MIN_LLEN, MAX_LLEN)
    num_terms = random.randint(MIN_SEARCH_TERMS, MAX_SEARCH_TERMS)
    search_occurance = 0.1
    search_keys = []

    while len(search_keys) < num_terms:
        search_key_len = random.randint(MIN_SEARCH_LEN, MAX_SEARCH_LEN)
        L1 = random.choice(string.ascii_letters)
        non_l1 = list(string.ascii_letters)
        non_l1.remove(L1)
        L2 = random.choice(non_l1)
        search_key = ''.join(
            [L1] * (search_key_len // 2) + [L2] * (search_key_len // 2))
        if search_key in search_keys:
            continue
        search_keys.append(search_key)


print(num_lines, num_terms)
print(*search_keys, sep=';')
for _ in range(num_lines):
    j = 0
    while j < line_len:
        search_key = search_keys[random.randint(0, len(search_keys) - 1)]
        insert_key = random.randint(0, 1) == 0
        if insert_key and (j + len(search_key)) <= line_len:
            print(search_key, end='')
            j += len(search_key)
        else:
            print(search_key[0], end='')
            j += 1
    print()
