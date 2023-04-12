import sys
N = int(sys.stdin.readline())

students = list(map(int,sys.stdin.readline().split(" ")))
B, C = map(int, sys.stdin.readline().split(" "))

teacher = N
for student in students:
    if student-B <=0:
        continue
    else:
        if (student-B)%C == 0:
            teacher += (student-B)//C
        else:
            teacher += (student-B)//C + 1

print(teacher)