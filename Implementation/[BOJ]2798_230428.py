from itertools import combinations 
N, M = map( int, input().split() )

cards = list( map ( int, input().split() ))

comb = combinations( cards, 3 )
MAX = 0

for c in comb:
    if sum(c) <= M:
       MAX = max( sum(c), MAX ) 


print(MAX)