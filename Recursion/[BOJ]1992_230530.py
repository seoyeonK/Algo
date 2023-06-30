import sys
input = sys.stdin.readline

N = int(input())
image = []

for n in range(N):
    image.append(list(input().rstrip()))

def quadTree(map):
    oneDim = []
    for row in map:
        oneDim += row

    if len(set(oneDim)) == 1 :
        return oneDim[0]


    if len(map) == 2:
        return '(' + ''.join(map[0]) + ''.join(map[1]) + ')'
    
    else:

        half = len(map) // 2

        up = map[:half]
        LU = [ x[:half] for x in up ] 
        RU = [ x[half:] for x in up ] 
        down = map[half:]
        LD = [ x[:half] for x in down ]
        RD = [ x[half:] for x in down ]

        return '(' + quadTree(LU) + quadTree(RU) + quadTree(LD) + quadTree(RD) + ')'

print(quadTree(image))