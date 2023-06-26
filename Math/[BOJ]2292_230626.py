N = int(input())

rooms = 0
num = 1

while True:
    num += rooms*6
    if N < num:
        break
    else:
        rooms += 1
    
print(rooms+1)