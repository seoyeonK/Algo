# R T 
# C F
# J M
# A N

# 3 - 2 - 1 - 0 - 1 - 2 - 3 

# survey = ["AN", "CF", "MJ", "RT", "NA"]
# choices = [5, 3, 2, 7, 5]

survey = ["TR", "RT", "TR"]
choices = [7,1,3]

def solution(survey, choices):
    answer = ''

    standard = ["RT", "CF", "JM", "AN"]
    measure = {"RT":0, "CF":0, "JM":0, "AN":0}    

    for i in range(len(survey)):    
        sorted_ = ''.join(sorted(survey[i]))  #which standard it is
        if survey[i] == sorted_:
            measure[sorted_] += choices[i]-4
        else :
            measure[sorted_] += 4 -choices[i]    
    

    for x in standard:
        if measure[x] <= 0 :
            answer += x[0]
        else:
            answer += x[1]
    return answer

print(solution(survey, choices))