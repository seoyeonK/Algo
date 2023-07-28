import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    user = []
    for i in range(N):
        age, name = input().split()
        age = int(age)
        user.append([age, name, i])
    user = sorted(user, key=lambda x: (x[0], x[2]))

    for u in user:
        print(u[0], u[1])

    return

solution() 