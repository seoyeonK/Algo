from collections import deque

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]] 

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            bfs(i,visited,computers,n)
            answer += 1
    return answer

def bfs(start, visited, computers,n):
    visited[start] = True
    queue = deque()
    queue.append(start)
    while queue:
        elem = queue.popleft()
        visited[elem] = True
        for i in range(n):
            if not visited[i] and computers[elem][i] == 1:
                visited[i] = True
                queue.append(i)

print(solution(n, computers))