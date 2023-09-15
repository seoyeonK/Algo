def dfs(depth, total, plus, sub, multi):
    global MIN, MAX
    if depth == n:
        MIN = min(MIN, total)
        MAX = max(MAX, total)
    
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, sub, multi)

    if sub:
        dfs(depth + 1, total - num[depth], plus, sub - 1, multi)
    
    if multi:
        dfs(depth + 1, total * num[depth], plus, sub, multi - 1)


n = int(input())

num = list(map(int, input().split()))
plus, sub, multi = map(int, input().split())

MIN, MAX = float("INF"), -float("INF")
dfs(1, num[0], plus, sub, multi)
print(MIN, MAX)