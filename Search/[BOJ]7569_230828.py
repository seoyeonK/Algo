from collections import deque

def solution():
    M, N, H = map(int, input().split()) #breadth, length, height
    tom = [ [ [] for _ in range(N)] for _ in range(H) ]
    ripe = []

    dr = [1, -1, 0, 0, 0, 0]
    dc = [0, 0, 1, -1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]

    queue = deque()
    day = 0
    
    green = 0

    for h in range(H):
        for n in range(N):
            tom[h][n] = list(map(int, input().split()))

            for m in range(M):
                if tom[h][n][m] == 1:
                    queue.append((h, n, m))
                elif tom[h][n][m] == 0 :
                    green += 1

    day = 0

    if green > 0 and len(queue) == 0 :
        day = -1

    elif len(queue) > 0:
        while queue:
            h, n, m = queue.popleft()

            for i in range(6):
                nh = h + dh[i]
                nn = n + dr[i]
                nm = m + dc[i]

                if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M : 
                    if tom[nh][nn][nm] == 0 :
                        tom[nh][nn][nm] = tom[h][n][m] + 1

                        queue.append((nh, nn, nm))

                        if tom[nh][nn][nm] > day:
                            day = tom[nh][nn][nm]

        for h in range(H):
            for n in range(N):
                if 0 in tom[h][n]:
                    day = -1
                    break
                
        if day > 0:
            day -= 1

    print(day)

solution()