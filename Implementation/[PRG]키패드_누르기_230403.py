# 1<= len(num) <= 1000


# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
# hand = "right"

# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = "left"

numbers = [1,2,3,4,5,6,7,8,9,0]
hand = "right"


def solution(numbers:list[int], hand:str)->str:
    answer = ''
    L = [3,0] # start = '*'
    R = [3,2] # start = '#'
    
    for num in numbers:
        if num in [1,4,7] : 
            answer += "L"
            L = [num//3, 0]
        elif num in [3,6,9] :
            answer += "R"
            R = [num//3-1, 2]
        else:
            if num == 0:
                num_ = [3,1]
            else:
                num_ = [num//3,1]
            D_L = abs(L[0]-num_[0]) + abs(L[1]-num_[1])
            D_R = abs(R[0]-num_[0]) + abs(R[1]-num_[1])

            if D_L == D_R:
                if hand == "left":
                    answer += "L"
                    L = num_
                else:
                    answer += "R"
                    R = num_
            elif D_L < D_R:
                answer += "L"
                L = num_
            else:
                answer += "R"
                R = num_          
            
    
    return answer

print(solution(numbers,hand))