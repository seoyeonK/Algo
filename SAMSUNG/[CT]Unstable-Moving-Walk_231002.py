from collections import deque

n, k = map(int, input().split())
stability = deque(list(map(int, input().split())))
people = deque([0 for i in range(n)])

zeros = 0

def simulate():
    global zeros

    # 무빙워크 이동
    stability.appendleft(stability.pop())
    people.appendleft(people.pop())

    # n번칸 사람 내리기
    if people[n - 1]:
        people[n - 1] = 0

    # 사람 이동
    for i in range(n - 1, 0, -1):
        # 현재 위치에 사람이 없고 내구도는 남아 있으면서 이전 위치에 사람이 있는 경우
        if people[i] == 0 and people[i - 1] and stability[i]:
            people[i] = 1
            people[i - 1] = 0

            stability[i] -= 1

            if stability[i] == 0:
                zeros += 1
    # n번칸 사람 내리기
    if people[n - 1]:
        people[n - 1] = 0

    # 사람 올리기
    if stability[0]:
        stability[0] -= 1
        people[0] = 1

        if stability[0] == 0:
            zeros += 1

answer = 0
while True:
    simulate()
    answer += 1

    if zeros >= k:
        break

print(answer)