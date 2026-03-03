import sys

sys.stdin = open('sample_input1.txt', 'r')

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    n_sum = 0

    for k in range(1, N+1):
        for part in combinations(arr, k):
            cnt += 1
            n_sum += sum(part)/k
    result = n_sum/cnt
    s = f"{result:.20f}".rstrip('0').rstrip('.')
    print(f'#{tc} {s}')