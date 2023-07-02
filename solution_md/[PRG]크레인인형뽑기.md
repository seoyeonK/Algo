# [PRG] 크레인 인형뽑기 게임

### 1. [문제](https://school.programmers.co.kr/learn/courses/30/lessons/64061)

- “N x N”크기의 격자에 있는 번호가 부여된 인형들을 바구니에 옮기는 인형뽑기 게임
- 인형은 바구니의 가장 아래 부터 순서대로 쌓임
- 같은 모양의 인형이 바구니에 연속해서 쌓이게 되면 두 인형은 바구니에서 사라짐
    
    **⇒ 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수?**
    
- 입력 :
    - 게임 화면의 격자의 상태가 담긴 2차원 배열 board
    - 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves
        
        
- 출력 : 터트려져 사라진 인형의 개수

### 2. 풀이

- 바구니 ⇒ stack!
- moves의 원소들을 m이라고 할 때, 입력으로 주어진 board를 그대로 사용하게 된다면,  m번째 위치의 원소를 매번 조회하고, 인형을 뽑게 됐을 경우의 처리 등이 코드적으로 비효율적
- 따라서 mvoe마다 board에서 m번에 위치한 인형들을 crane이라는 list로 생성하여 사용한다.
- 이 때, crane의 가장 윗부분에 있는 인형을 뽑기 위해 for loop을 이용
    - 만약 basket이 비어있거나, basket의 가장 위에 위치한 인형이 방금 뽑은 인형과 다를 경우, basket에 방금 뽑은 인형을 append
    - 만약  basket의 가장 위에 위치한 인형이 방금 뽑은 인형과 같을 경우 인형을 없앤 후 answer +=2

### 3. 코드

```python
def solution(board, moves):
    answer = 0
    
    basket = []
    
    width = len(board)
    
    for m in moves:
        crane = [ board[x][m-1] for x in range(width) ] 
        
        for i in range(width):
            if crane[i] != 0:
                board[i][m-1] = 0
                
                if not basket or crane[i] != basket[-1]:
                    basket.append(crane[i])
                else:
                    basket.pop(-1)
                    answer += 2
                break
                      
    return answer
```

### +α