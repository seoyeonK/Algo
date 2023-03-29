

# 1<= s길이 <= 50

#s = "one4seveneight"
s = "23four5six7"
# s = "2three45sixseven"
# s = "123"


# 내 답
def solution1(s):
    answer = 0
    alph = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    temp =""
    for i in range(len(s)):         
        if 48 <= ord(s[i]) and ord(s[i]) <= 57:
            answer = answer*10 + (ord(s[i])-48)
        else:
            temp+=s[i]
        if temp in alph:
            answer = answer*10 + alph.index(temp)
            temp =""
        
    return answer

#모범답안^^
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


print(solution(s))

# print("o" + "n")