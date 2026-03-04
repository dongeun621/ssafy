import sys

sys.stdin = open('sample_input4.txt', 'r')

from itertools import permutations
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    arr = [x for x in range(N)]
    result = 999
    for j_list in permutations(arr, N):
        n_sum = 0
        for i in range(N):
            n_sum += matrix[i][j_list[i]]
        result = min(result, n_sum)
    print(f'#{tc} {result}')