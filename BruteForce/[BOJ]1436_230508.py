N = int(input())

def shom(N):
    result = '666'
    if N > 1:
        result = str(N-1) + result
    return result
print(shom(N))