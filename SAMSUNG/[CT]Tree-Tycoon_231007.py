n, m = map(int, input().split())

trees = [ list(map(int, input().split())) for _ in range(n) ]
moves = [ tuple(map(int, input().split())) for _ in range(m) ]

#     → ↗  ↑  ↖  ← ↙ ↓ ↘
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

sur_r = [-1, -1, 1, 1]
sur_c = [-1, 1, -1, 1]

def moved(x):
    if x < 0:
        x =  x + n
    elif x >= n:
        x = x % n
    return x

nutri = {(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)}

for d_idx, leng in moves:
    
    d_idx -= 1
    
    new = set()

    for r, c in nutri:
        nr = moved(r + dr[d_idx] * leng)
        nc = moved(c + dc[d_idx] * leng)
        
        trees[nr][nc] += 1

        new.add((nr,nc))
        
    for r, c in new:
        surround = 0
        for i in range(4):
            n_r = r + sur_r[i]
            n_c = c + sur_c[i]
            if 0 <= n_r < n and 0 <= n_c < n and trees[n_r][n_c] >= 1:
                surround += 1
        trees[r][c] += surround

    nutri.clear()
    for i in range(n):
        for j in range(n):
            if (i,j) not in nutri and trees[i][j] >= 2:
                trees[i][j] -= 2
                nutri.add((i,j))
    
print(sum(sum(e) for e in trees))
