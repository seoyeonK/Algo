import sys, collections
input = sys.stdin.readline


def solution():
    anna = collections.defaultdict(list)
    words = []
    while True:
        w = input().rstrip()
        if w == 'EOF':
            break

        words.append(w)

    for w in words:
        k = ''.join(sorted(w))

        if k in anna.keys() and w not in anna[k]:
            anna[k].append(w)
        else:
            anna[k] = [w]

    tmp = []

    for k in anna.keys():
        anna[k].sort()
        tmp.append(anna[k])


    tmp.sort(key = lambda x : (-len(x), x[0]))

    for i in range(5):
        print(f'Group of size {len(tmp[i])}:',*tmp[i],'.')
solution()