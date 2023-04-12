N = int(input())

count = 1
add = 1

while N > add:
    add += 6*count
    count +=1

print(count)
#1 1
#2 2 - 7 :   6*0 + 2 ~ 6*1+1
#3 8 - 19 :  6*1 + 1  ~  6*3 +1
#4 20 - 37 : 6*3 + 2 ~6*6 + 1
#5 38 - 61  : 24    6*10 + 1
