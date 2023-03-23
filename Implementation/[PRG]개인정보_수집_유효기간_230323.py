today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

t_y, t_m, t_d = map(int,today.split("."))
t_dys = t_y*12*28 + t_m*28 + t_d

Term = {} # {'A' : 6}
#expired = []

answer = []

for term in terms:
    x, y = term.split(" ")
    Term[x] = int(y)*28


for i in range(len(privacies)):
    p_date, t_ = privacies[i].split(" ")
    p_y, p_m, p_d = map(int, p_date.split("."))
    p_days = p_y*12*28 + p_m*28 + p_d

    if p_days + Term[t_] <= t_dys :
        answer.append(i+1)

    #dur = p_m + Term[t_]
    
    # if dur % 12 == 0 :
    #     end_y = p_y + (dur // 12 - 1)
    #     end_m = 12
    # else:
    #     end_y = p_y + dur // 12
    #     end_m = dur % 12
    
    
    # if t_y > end_y or (t_y == end_y and t_m > end_m) or (t_y == end_y and t_m == end_m and t_d >= p_d):
    #     expired.append(i+1)

# print(expired)
print(answer)


