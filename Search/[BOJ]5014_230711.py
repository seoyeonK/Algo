from  collections import deque

def solution():
    F, S, G, U, D = map(int, input().split())

    visited = [False] * (F + 1)

    visited[S] = True
    btn = 0

    queue = deque()
    queue.append((S, btn))
    results = []
    button = [U, -D]

    while queue:
        cur, btn = queue.popleft()
        if cur == G :
            results.append(btn)
            continue
        for i in range(2):
            next = cur + button[i]

            if 1 <= next <= F and not visited[next]:
                queue.append((next, btn + 1))
                visited[next] = True
    
    
    results = sorted(results)

    if not results:
        print('use the stairs')
    
    else:
        print(results[0])

solution()