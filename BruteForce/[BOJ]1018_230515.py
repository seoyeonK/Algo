import sys
input = sys.stdin.readline
N, M = map(int, input().split()) #행 열

board = [ list(input()) for _ in range(N)]


def swapColor(color):
    if color == 'W':
        return 'B'
    else:
        return 'W'

def BF(N,M):
    result = []
    for r_s in range(N-7):
        for c_s in range(M-7):
            count1 = 0
            count2 = 0
            for r in range(r_s, r_s + 8):            
                for c in range(c_s, c_s + 8):
                    if (r + c) % 2 == 0:
                        if board[r][c] != 'B':
                            count1 += 1
                        if board[r][c] != 'W':
                            count2 += 1
                    else:
                        if board[r][c] != 'W':
                            count1 += 1
                        if board[r][c] != 'B':
                            count2 += 1
            result.append(count1)
            result.append(count2)

    print(min(result))

BF(N,M)