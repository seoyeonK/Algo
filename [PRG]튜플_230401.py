# tuple 
#    can have duplicates
#    order matters
#    length limited

#  5 <=  len(s) = n  <= 1,000,000 ,  no duplicates 


# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"     #[2, 1, 3, 4]
# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"    #[2, 1, 3, 4]
# s = "{{20,111},{111}}"                 #[111,20]


# s = "{{123}}"
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"	#[3, 2, 4, 1]

def solution(s):
    answer = []
    hash = {}

    s_list = s[1:-1].split("},{")  
    for set in s_list:
        set_list = set.replace("{","").replace("}","").split(",")
        for i in set_list:
            if i in hash.keys():
                hash[i] +=1
            else:
                hash[i] = 1

    def my_sort(x):
        return hash[x]
    
    answer = list(hash.keys())
    answer.sort(reverse=True,key=my_sort)   
    
    answer = list(map(int,answer))

    return answer


# print(solution(s))


#다른 풀이
def solution_1(s):
    answer = []
    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1 : 
        new_s.append(i.split(','))

    new_s.sort(key = len, reverse=True)

    for i in new_s :
        for j in range(len(i)):
            if int(i[j]) not in answer : 
                answer.append(int(i[j]))
    return answer

# print(solution_1(s))
    



#레전드 코드
import re
from collections import Counter

def solution_2(s):

    s = Counter(re.findall('\d+', s))   #숫자만 걷어내기 미친....ㅋㅋㅋ
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
