n = int(input())
work = [ list(map(int, input().split())) for _ in range(n) ]

def calc(lst):
    workload = 0
    for i in range(n//2):
        for j in range(i, n//2):
            workload += work[lst[i]][lst[j]]
            workload += work[lst[j]][lst[i]]

    return workload

def dfs(depth, one, two):
    global answer
    if depth == n :
        if len(one) == len(two):
            answer = min(answer, abs(calc(one) - calc(two)))
        return
    
    dfs(depth + 1, one + [depth], two)
    dfs(depth + 1, one, two + [depth])
    

answer = float("INF")
dfs(0, [], [])

print(answer)