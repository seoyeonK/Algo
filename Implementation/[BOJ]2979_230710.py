import sys

def solution():
    input = sys.stdin.readline

    A, B, C = map(int, input().split())

    truck = [0] * 101

    for _ in range(3):
        enter, exit = map(int, input().split())
        for i in range(enter, exit):
            truck[i] += 1
            
    ticket = A * truck.count(1) * 1 + B * truck.count(2) * 2 + C * truck.count(3) * 3

    print(ticket)

    return

solution()