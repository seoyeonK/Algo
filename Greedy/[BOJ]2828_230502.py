N, M = map(int, input().split())
J = int(input())

cur = 0
moves = 0
for i in range(J):
    apple = int(input()) -1  #index of apple
    if cur <= apple < cur + M:
        continue
    elif apple < cur:
        moves += cur - apple
        cur = apple
    else: 
        moves += apple - cur - M + 1
        cur = apple - M + 1

print(moves)

# baskets = [1]*M + [0]*(N-M) 
# def findBasket(apple): #find index of basket's edge
#     for i in range(1,N-1):
#         if 0 <= apple-i < N and baskets[apple-i] == 1:
#             return -i
#         elif 0 <= apple+i < N and baskets[apple+i] == 1:
#             return i


# moves = 0
# for i in range(J):
#     apple = int(input()) -1  #index of apple
#     if baskets[apple] == 1:  #if there is a basket on the bottom
#         continue
#     else:
#         move = findBasket(apple)
#         if move < 0:
#             baskets = [0]*(apple-M+1) + [1]*M + [0]*(N-apple-1)
#         else: 
#             baskets = [0]*(apple) + [1]*M + [0]*(N-apple-M)
#         moves += abs(move)





