def solution():
    a, b = map(int, input().split())
    lcm = a * b
    while b > 0:
        a, b = b, a%b
    gcd = a
    lcm //= gcd

    print(gcd)
    print(lcm)
    
solution()