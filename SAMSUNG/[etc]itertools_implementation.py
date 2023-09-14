import itertools

# 1-1. itertools.permutations
test2 = ['A', 'B', 'C']

permutations_test = list(map(''.join, itertools.combinations(test2,2)))



# 1-2. permutations implementation
def permutations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutations(arr[:i] + arr[i+1:], r-1):
                yield [arr[i]] + next
                
                
                
                
                
# 2-1. itertools.combinations
test1 = ['A', 'B', 'C']

combination_test = list(map(''.join, itertools.combinations(test1,2)))


# 2-2. combinations implementation

def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):
                yield [arr[i]] + next
       

print(list(combinations(test1, 2)))
       
        

                
#https://velog.io/@yeseolee/python%EC%9C%BC%EB%A1%9C-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9-%EC%A7%81%EC%A0%91-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0