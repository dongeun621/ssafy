import sys

sys.stdin = open('sample_input2.txt', 'r')

from itertools import permutations, combinations
T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
 
    for i in range(N):
        for a in combinations(arr, i):
            if sum(a) == K:
                result += 1
 
    print(f'#{tc} {result}')