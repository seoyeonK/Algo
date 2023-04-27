from collections import deque

F, S, G, U, D = map(int, input().split())

d = [0]*(F+1)
d[S] = 1

def bfs(s):
    q = deque()
    q.append(s)
    while q:
        cur = q.popleft()
        if cur == G:
            return d[cur]-1
        for next in [cur+U, cur-D]:
            if 0<= next <= F and not d[next]:
                d[next] = d[cur] +1
                q.append(next)
    if d[G]==0:
        return "use the stairs"

print(bfs(S))