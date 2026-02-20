import sys

sys.stdin = open('sample_input5.txt', 'r')

from itertools import combinations, permutations
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    N_list = set(i for i in range(N))
    com_N = list(combinations(N_list, int(N/2)))
    result = 99999999999999999
    #A,B의 음식 조합 경우의 수
    for a in com_N:
        a = set(a)
        b = N_list-a
        com_a = list(permutations(a, 2))
        com_b = list(permutations(b, 2))
        #2가지 음식조합의 점수 추출 및 합산
        sum_a = 0
        sum_b = 0
        for i,j in com_a:
            sum_a += matrix[i][j]
 
        for i,j in com_b:
            sum_b += matrix[i][j]
        result = min(result, abs(sum_a-sum_b))
    print(f'#{tc} {result}')