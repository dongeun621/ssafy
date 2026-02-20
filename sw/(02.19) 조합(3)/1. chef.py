import sys

sys.stdin = open('sample_input1.txt', 'r')

from itertools import permutations, combinations
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    arr = set(i for i in range(N))
    n = int(N/2)
    result = 9999999
 
    for a in combinations(arr, n):
        b = arr-set(a)
        a_sum = 0
        b_sum = 0
        for i,j in permutations(a, 2):
            a_sum += matrix[i][j]
        for i,j in permutations(b, 2):
            b_sum += matrix[i][j]
        result = min(result, abs(a_sum-b_sum))
    print(f'#{tc} {result}')