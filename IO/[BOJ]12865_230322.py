# input : 
#   N개 물건, 최대 무게 K
#   무게 W, 가치 V 
# max V = ?
# constraints : 1<= N <= 100,  1<= K <= 100000   
# 1<= W <=100000   0<= V <= 1000

# ref : https://www.youtube.com/watch?v=uggO0uzGboY

# table[i][j+w[i]] = max(table[i-1][j+w[i]], table[i-1][j] + v[i])

def solve(): 
    n, k = map(int, input().split())
    table = [0] * (k+1)
    for _ in range(n):
        w, v = map (int, input().split())
        if w > k : 
            continue
        for j in range(k, 0, -1):
            if j+w <= k and table[j] != 0 : 
                table[j+w] = max(table[j+w], table[j]+v)
        table[w] = max(table[w],v)
    print(max(table))

solve()