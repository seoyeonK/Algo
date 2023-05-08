import sys
T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
    # a = sys.stdin.readline().split()
    # sys.stdout.write("%d\n" %(int(a[0]) + int(a[1])))