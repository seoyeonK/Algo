# 1/1   
# 1/2
# 2/1   
# 3/1   2/2     1/3     
# 1/4   2/3     3/2      4/1
# 5/1   4/2     3/3      2/4    1/5

X = int(input())

dir = True # T : right, F : left
top = 1
btm = 1
turned = False
end = 1

if X > 1:
    btm += 1
    for i in range(2,X):
        end += i
        if X <= end:
            diff = end - X
            if i % 2 == 0 : #left
                top = i - diff
                btm = 1 + diff
            else:
                top = 1 + diff
                btm = i - diff
            break


print(str(top)+'/'+str(btm))