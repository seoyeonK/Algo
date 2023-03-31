# 3<= id_len <=15
# alphabet_lower, num, - , _ , .   ( . <- can't come in first/last, and in succession)

# new_id = "...!@BaT#*..y.abcdefghijklm." 
# new_id = "z-+.^."
#new_id = "=.= "
# new_id = "123_.def"
# new_id = "abcdefghijklmn.p"
# new_id = "......a......a......a....."
new_id =  "-.~!@#$%&*()=+[{]}:?,<>/.-"


def solution(new_id):
    answer = ''
    nums = ['1','2','3','4','5','6','7','8','9','0']
    special = ['-', '_', '.']

    # step1
    new_id = new_id.lower()
    
    # step2
    for char in new_id:
        if (ord(char) < 97 or ord(char) > 122) and (char not in special) and (char not in nums) :
            new_id = new_id.replace(char,'')

    #step3
    while True:
        new_id = new_id.replace('..','.')
        if '..' not in new_id:
            break

    #step4
    if len(new_id)>1:
        if new_id[0] == '.' :
            new_id = new_id[1:]
        if new_id[-1] == '.' :
            new_id = new_id[:-1]
        
    if new_id == ".":
        new_id = ""

    #step5
    if len(new_id) == 0:
        new_id = "a"
    
    #step6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.' :
            new_id = new_id[:-1]

    #step7
    if len(new_id) <= 2:
        last = new_id[-1]
        while True:
            new_id += last
            if len(new_id) == 3:
                break

    answer = new_id
    return answer

print(solution(new_id))


#with regex : https://velog.io/@nellroll/%EC%8B%A0%EA%B7%9C-%EC%95%84%EC%9D%B4%EB%94%94-%EC%B6%94%EC%B2%9C
import re

def solution_regex(new_id):
    answer = ''
    
    # re.sub('정규표현식',치환문자,대상문자열)
    # 소문자로 바꾼 문자열을 대상으로 알파벳이나 숫자가 아니면 / '_' , '-', '.' 이 아니면 빈값으로 치환
    answer = re.sub('[^a-z\d\_\-\.]','',new_id.lower())  

    # 마침표 . 이 2번 이상 연달아 있을 경우 1개로 대체
    answer = re.sub('\.\.+', '.', answer) 

    # 마침표로 시작하면 제거 
    answer = re.sub('^\.', '', answer)

    # 빈 문자열이면 'a'
    if answer == '':
        answer = 'a'
    
    # 마침표로 끝난다면 & 길이가 16이상이라면 다 끊어내기
    answer = re.sub('\.$','', answer[:15])
    
    #길이가 2이하면 마지막 문자를 길이가 3이 될때까지 이어붙이기
    if len(answer) < 3:
        return answer.ljust(3, answer[-1])

    return answer