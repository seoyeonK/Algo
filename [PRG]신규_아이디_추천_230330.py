# 3<= id_len <=15
# alphabet_lower, num, - , _ , .   ( . <- can't come in first/last, and in succession)

# new_id = "...!@BaT#*..y.abcdefghijklm." 
# new_id = "z-+.^."
#new_id = "=.= "
# new_id = "123_.def"
new_id = "abcdefghijklmn.p"


def solution(new_id):
    answer = ''
    nums = ['1','2','3','4','5','6','7','8','9','0']
    special = ['-', '_', ',', '.']

    # step1
    new_id = new_id.lower()
    
    # step2
    for char in new_id:
        if (ord(char) < 97 or ord(char) > 122) and \
            (char not in special) and (char not in nums) :
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


# 테케 실패 : 15, 20, 21, 22, 25