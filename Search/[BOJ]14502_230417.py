#0 
#1 벽
#2 qkdlfjtm
import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, M = map(int, sys.stdin.readline().split())
graph = [[]*M]*N
visited = []


def bfs(node, count):
    visited[node] = True
    

for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))

