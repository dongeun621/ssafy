import sys

sys.stdin = open('sample_input5.txt', 'r')

from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [x for x in range(1,13)]
    cnt = 0
    for a in combinations(arr, N):
        if sum(a) == K:
            cnt += 1
    print(f'#{tc} {cnt}')
