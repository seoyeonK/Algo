#n개 층 식당 고객 체온 측정 
# 검사팀장 + 검사 팀원
# 1가게당 팀장 1 (필수), 팀장 2~
import math

n = int(input())
clients = list(map(int, input().split()))
lead, member = map(int, input().split())

answer = 0

for client in clients:
    if lead >= client :
        answer += 1
    
    else:
        answer += 1 + math.ceil((client - lead)/member)

print(answer)