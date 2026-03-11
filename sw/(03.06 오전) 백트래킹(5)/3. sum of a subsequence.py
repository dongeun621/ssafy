import sys

sys.stdin = open('sample_input3.txt', 'r')

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    for k in range(N):
        for a in combinations(arr,k+1):
            if sum(a) == K:
                result += 1
    print(f'#{tc} {result}')