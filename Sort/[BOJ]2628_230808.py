import sys
input = sys.stdin.readline

def sol():

    w, h = map(int, input().split())

    cut = int(input())

    hor = [0,w]  # [2,3]
    ver = [0,h]  # [4]

    for _ in range(cut):
        dir, num = map(int, input().split())
        if dir == 1:
            hor.append(num)
        else:
            ver.append(num)

    hor.sort()
    ver.sort()

    max_w = hor[1]
    max_h = ver[1]

    for i in range(len(hor)-1):
        if max_w < hor[i+1] - hor[i]:
            max_w = hor[i+1] - hor[i]

    for i in range(len(ver)-1):
        if max_h < ver[i+1] - ver[i]:
            max_h = ver[i+1] - ver[i]

    print(max_h * max_w)

sol()