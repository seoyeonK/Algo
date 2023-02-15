# 단어를 애너그램 그룹으로 나누기.... 알파벳의 순서를 바꿔서 같은 단어가 되는 애들의 그룹
# 그룹의 크기 = 그 그룹에 포함된 단어의 수 
# 단어가 주어졌을 때 크기가 가장 큰 애너그룹 다섯개를 구하기
# 입력 최대 30,000줄 , EOF로 끝남
# 그룹의 크기가 감소하는 순으로, 크기가 같으면 각 그룹에서 가장 사전순으로 앞서는 단어의 사전 순으로, 같은 단어는 한버만 출력'


# import sys

# words = [line.strip() for line in sys.stdin]

# alphas = []

# for i in range(len(words)):
#     temp = list(words[i])
#     alphas[i] = temp.sort()

# result = {}

# for i in range(len(words)-1):
#     temp = []
#     temp[0] = words[i]
#     for j in range(i+1, len(words)):
#         if alphas[i] == alphas[j] :
#             temp.append(words[j])
#     temp.sort()
#     result[temp[0]] = temp
import collections
 
anagrams = collections.defaultdict(list)
li = []
tmp = []
 
while True:
    try:
        word = input()
        li.append(word)
    except EOFError:
        break
 
for i in li:
    anagrams["".join(sorted(i))].append(i)
 
max_len = -1

for i in anagrams.keys():
    sorted_anagram = sorted(anagrams[i])
    max_len = max(max_len, len(sorted_anagram))
    tmp.append(sorted_anagram)
tmp.sort(key=lambda x: (max_len - len(x), x[0])) #크기별로 나열 & 사전 순으로 나열
for i in range(min(len(tmp), 5)):
    print(f'Group of size {len(tmp[i])}: {" ".join([elem for elem in sorted(list(set(tmp[i])))])} .')