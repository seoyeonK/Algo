def solution():

  N = int(input())
  T = []
  P = []
  
  for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
  
  day = [0] * (N + 1)
  
  for i in range(N):
    for j in range(i + T[i], N + 1):
      if day[j] < day[i] + P[i]:
        day[j] = day[i] + P[i]
        
  print(day[-1])

solution()
