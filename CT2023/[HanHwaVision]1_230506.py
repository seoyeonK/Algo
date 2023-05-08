from itertools import combinations
# REF : https://sunnnny.notion.site/230506-701b114a65e541f09ee6bb52e664f720


N = 10
deck = [2,5,6,8]

def makeGroup(deckList):
    groups = []
    temp = [deckList[0]]
    if len(deckList) == 1:
        return deckList
    else:
        for i in range(1, len(deckList)):
            if deckList[i] == deckList[i-1] + 1:
                temp.append(deckList[i])
            else:
                groups.append(temp)
                temp = [deckList[i]]
    return groups
print(makeGroup([1,2,4,6,7]))
    


def solution(N, deck):
    answer = []
    options = list(set([i for i in range(1,N+1)]) - set(deck))
    



    for i in range(len(options)):
        cards = combinations(options,i)


    return answer

print(solution(N, deck))