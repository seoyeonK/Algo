id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]      
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

#result = [2,1,1,0]   메일을 받은 횟수

# id_list 길이 2<=  <=1000
#  report 길이 1<=  <=200,000


# 시간초과 
# record = dict로 {'user' : [[신고한_사람_list], 신고당한_횟수]]} 
# for문으로 record에서 신고당한 횟수가 k보다 크면 record의 신고한_사람_list에 
#해당 사용자가 있을 경우 - id_list의 인덱스와 같은 result의 인덱스에 +1

# => O( id_list의 길이 * report의 길이 ) -> 최대 O(200,000,000) 


def solution_1(id_list, report, k):
    record = {}
    answer = [0]*len(id_list)

    for id in id_list:
        record[id] = []  #id : "who reported"    (not whom the id reported)

    for r in report :
        id, reported = r.split(" ")
        if id in record[reported] : 
            continue
        else:
            record[reported].append(id)
    
    for id in record.keys():
        if len(record[id]) >= k:
            for user in record[id]:
                idx = id_list.index(user)
                answer[idx] +=1

    return answer



print(solution_1(id_list, report, k))




# 다른 사람 풀이
def solution_2(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer