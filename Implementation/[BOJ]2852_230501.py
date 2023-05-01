import sys

def timeToNum(time):
    min, sec = map(int, time.split(":"))
    return min * 60 + sec

def numToTime(sec):
    min = str(sec // 60)
    sec = str(sec % 60)
    if len(min) == 1:
        min = "0" + min
    if len(sec) == 1:
        sec = "0" + sec
    return min + ":" + sec

N = int(sys.stdin.readline())
goals = {}
score = [0, 0]
winDur = [0, 0]

for n in range(N):
    team, time = sys.stdin.readline().split(" ")
    team = int(team)
    goals[timeToNum(time)] = team


for i in range(0, timeToNum("48:00")) :
    if i in goals:
        score[goals[i] - 1] += 1

    if score[0] > score[1]:
        winDur[0] += 1
    elif score[0] < score[1]:
        winDur[1] += 1
    
print(numToTime(winDur[0]))
print(numToTime(winDur[1]))