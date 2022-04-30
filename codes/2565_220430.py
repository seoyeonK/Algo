"""
두 전봇대 A, B사이에 교차 없이 전깃줄 연결해야됨

전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서 차례대로 번호가 매겨짐
전깃줄의 개수와 연결되는 위치의 번호가 주어졌을 때 전깃줄이 서로 교차하기 않게 하기 위해 없애야하는 전기줄의 최소 개수?


input : 전깃줄 개수 (100이하의 자연수) + A,B 연결되는 위치 번화 차례대로 한줄씩 
(공백 구분, 위치 번호는 500이하의 자연수, 같은 위치에 두개 이상의 전깃줄 연결 불가)
ex: 

8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6

output : 교차없이 연결하기 위해 제거해야되는 전깃줄 개수

ex: 3


"""
import sys
n = int(sys.stdin.readline())

lines = []

for i in range(n):
    lines.append(list(map(int, sys.stdin.readline().split())))

lines.sort(key = lambda x: x[0])
#LIS
rst = [1]*n # 가장 긴, 증가하는 subset의 길이를 담는 리스트
for i in range(1, n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            rst[i] = max(rst[i], rst[j]+1)

print(n - max(rst))
