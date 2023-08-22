def solution():
  T = int(input())
  
  for _ in range(T):
    k = int(input())
    n = int(input())
    #k층 n호
    
    apt = [i for i in range(n+1)]
  
    for i in range(k) :
      for j in range(2,n+1) :
        apt[j] += apt[j-1]
  
    print(apt[-1])

solution()
