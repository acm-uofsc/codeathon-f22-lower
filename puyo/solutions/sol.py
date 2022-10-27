y_dim, x_dim = map(int, input().split())
board = [list(map(int,input().split())) for y in range(y_dim)]
ever_seen = set()
cur_streak = set()
FILLER = 0

adj4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ret = set()
def dfs(y, x, to_find, board):
    cur = (y, x)
    if cur in ever_seen or board[y][x] != to_find or board[y][x] == FILLER:
        return
    ever_seen.add(cur)
    cur_streak.add(cur)
    for dy, dx in adj4:
        new_y = y + dy
        new_x = x + dx
        if new_y in range(y_dim) and new_x in range(x_dim):
            dfs(new_y, new_x, to_find, board)
        
for y in range(y_dim):
    for x in range(x_dim):
        cur_streak.clear()
        dfs(y, x, board[y][x], board)
        if len(cur_streak) >= 4:
            ret |= cur_streak

for y, x in sorted(ret):
    print(y, x)
