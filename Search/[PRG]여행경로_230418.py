from collections import defaultdict
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# >> return : ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

def solution(tickets):
    answer = []
    tic = defaultdict(list)

    for t in tickets:
        tic[t[0]].append(t[1])

    for k in tic.keys():
        tic[k].sort(reverse=True)
    

    route = []
    stack = ["ICN"]
    while stack:
        top = stack.pop()
        if top not in tic or not len(tic[top]):
            route.append(top)
        else:
            stack.append(top)
            stack.append(tic[top][-1])
            tic[top] = tic[top][:-1]
    return route[::-1]


    return answer