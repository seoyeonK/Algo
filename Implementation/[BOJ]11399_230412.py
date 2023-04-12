N = int(input())
times = list(map(int, input().split(" ")))
#times = sorted(list(map(int, input().split(" "))))

def quick_sort(times):
    if len(times)<=1:
        return times
    pivot = times[0]
    tail = times[1:]

    left = [ x for x in tail if x < pivot ]
    right = [ x for x in tail if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


times_ = quick_sort(times)

answer = 0
for i in range(N):
    answer += times_[i]*(N-i)

print(answer)
