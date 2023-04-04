from collections import deque
import sys
from tkinter import E
# https://www.notion.so/sunnnny/DFS-BFS-2d1c6b6245e2496492ec08649150cdc7#40b2a4ec600544f0a29baf833ca9ea80

# 0. DFS 
graph_01 = [ 
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited_0 = [False] * len(graph_01)
def dfs_0(graph:list[list], v:bool, visited:list[bool]):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs_0(graph,i,visited)
dfs_0(graph_01,1,visited_0)


#0. BFS

graph_01 = [ 
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited_01 = [False]*len(graph_01)
def bfs_0(graph, start, visited):
    queue_0 = deque([start])
    visited[start] = True
    while queue_0:
        v = queue_0.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue_0.append[i]
                visited[i] = True




# 1. 음료수 얼려먹기
N,M = 4,5   #  map(int,sys.stdin.readline().split(" "))
cubes = []

# for i in range(N):
#     cubes.append(list(map(int,input())))

def dfs(x,y) : 
    if x <= -1 or x >= N or y <= -1 or y >= M :
        return False
    
    if cubes[x][y] == 0:    #현재 노드를 아직 방문하지 않았다면
        cubes[x][y] = 1     #방문 처리

        dfs(x-1, y)         #상하좌우의 위치들도 재귀적으로 호출
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True : 
            result += 1




# 2. 미로탈출
N,M = map(int,sys.stdin.readline().split(" "))
graph = []

for i in range(N):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue :
        x,y = queue.popleft()

        for i in range(4):      # 현재 위치에서 상하좌우 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M : #범위 밖이면 무시
                continue
            
            if nx == 0 and ny == 0 :    # 다시 시작점으로 돌아가는 것 방지
                continue

            if graph[nx][ny] == 0 :     #괴물인 경우 무시
                continue

            if graph[nx][ny] == 1:      #해당 경우 처음 방문하는 경우에만 최단 거리 기록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[N-1][M-1]

print(bfs(0,0))
