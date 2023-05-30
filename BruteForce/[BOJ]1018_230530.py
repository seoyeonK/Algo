import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [[] for _ in range(N)]

for n in range(N):
    board[n] = list(input().rstrip())

answer = []

for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0 
        cnt2 = 0
        for r in range(i, i+8):
            for c in range(j, j+8):
                if (r+c) % 2 == 0:
                    if board[r][c] != 'W':
                        cnt1 += 1
                    elif board[r][c] != 'B':
                        cnt2 += 1
                else:
                    if board[r][c] != 'B':
                        cnt1 += 1
                    elif board[r][c] != 'W':
                        cnt2 += 1
        answer.append(cnt1)
        answer.append(cnt2)

print(min(answer))