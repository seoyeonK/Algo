n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
 # 0:blank, 1:person, 2:hospital
people = []
hospital = []

for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            people.append((r,c))
        elif graph[r][c] == 2:
            hospital.append((r,c))

len_h = len(hospital)
visited = [False] * len_h
result = float("INF")

def calc():
    res = 0
    for pr,pc in people:
        minh = 2 * n
        for i in range(len_h):
            if visited[i]:
                hr, hc = hospital[i][0], hospital[i][1]
                h = abs(pr - hr) + abs(pc - hc)
                minh = min(minh, h)
        res += minh
    return res
        

def dfs(depth, last_idx):
    global result, remain
    if depth == m:
        result = min(result, calc())
        return

    for i in range(last_idx + 1, len_h):
        visited[i] = True
        dfs(depth + 1, i)
        visited[i] = False

dfs(0, -1)

print(result)