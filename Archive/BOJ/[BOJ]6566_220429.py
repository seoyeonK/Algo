import collections

anagrams = collections.defaultdict(list)

li = []

while True:
    try: 
        word = input()
        li.append(word)
    except EOFError:
        break

for i in li:
    anagrams["".join(sorted(i))].append(i)

max_len = -1

tmp = []

for i in anagrams.keys():
    anagrams[i].sort() # 각 key에 해당하는 value들 정렬
    max_len = max(max_len, len(anagrams[i]))
    tmp.append(anagrams[i])

tmp.sort(key = lambda x : (max_len - len(x), x[0])) # 크기순 정렬 후 사전순

for i in range(min(len(tmp),5)):
    print(f'Group of size {len(tmp[i])}: { " ".join ([elem for elem in sorted(list(set(tmp[i])))])} .')