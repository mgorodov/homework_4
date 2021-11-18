from random import randint


def partition(a, left, right):
    q = a[(left + right) // 2]
    i = left
    j = right
    while True:
        while a[i] < q:
            i += 1
        while a[j] > q:
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


def kth_statistic(a, k):
    lo = 0
    hi = len(a) - 1
    while True:
        p = partition(a, lo, hi)
        if p == k:
            return a[p]
        elif k < p:
            hi = p
        else:
            lo = p + 1


LOW = -100
HIGH = 100
NUMBER = 1000

correct_cnt = 0
for _ in range(1, NUMBER + 1):
    inp = [randint(LOW, HIGH) for i in range(_)]
    arr = inp
    srt = sorted(inp)

    m = kth_statistic(arr, _ // 2)
    if m == srt[_ // 2]:
        correct_cnt += 1

    # print("%4d %4d" % (m, srt[_ // 2]), ' Src:', *inp, ' Array:', *arr, ' Sorted:', *srt)

print("Correct rate: ", 100 * (correct_cnt / NUMBER), '%', sep='')
