# 재귀를 이용해서 조합과 순열을 구할 수 있다.

# 기본적인 아이디어는 다음과 같다. DFS, 백트래킹과 상당히 유사하다.

# combination([0,1,2,3], 2) = ([0],combination([1,2,3], 1)) + ([1],combination([2,3], 1)) + ([2],combination([3], 1)))
# permutation([0,1,2,3], 2) = ([0],permutation([1,2,3], 1)) + ([1],permutation([0,2,3], 1)) + ([2],permutation([0,1,3], 1))+ ([3],permutation([0,1,2], 1))


#1. itertools
from itertools import combinations

arr = [0, 1, 2, 3, 4, 5]

print(list(combinations(arr, 3)))


from itertools import permutations
print(list(permutations(arr, 3)))



#2. 구현하기

def gen_combinations(arr, n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1): 
            result.append([elem]+C) 
              
    return result


def gen_permutations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i, elem in enumerate(arr): 
        for P in gen_permutations(arr[:i] + arr[i+1:], n-1):
            result += [[elem]+P]
              
    return result
    
    
arr = [0, 1, 2, 3, 4, 5]

print(gen_permutations(arr, 3))






def permu(arr, k):
    result = []
    if k == 0:
        return [[]]
    
    for i, elem in enumerate(arr):
        for P in permu(arr[:i]+arr[i+1:], k-1):
            result += [[elem]+P]