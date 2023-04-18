def evenOrOdd(num):
    return "Even" if num%2==0 else "Odd"


#2진 비트에서 1번째 비트자리에 의해 홀짝 결정
# & 연산자로 0 과 1을 구해 리스트 인덱스로

def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]


 