import sys

sys.stdin = open('sample_input8.txt', 'r')

from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sum_ij = []
    result = 0
    for i in range(N):
        for j in range(N-M+1):
            max_sum = 0
            #좌표별 최대갑 구하기
            for k in range(M):
                #combinations 경우의 수 구하기
                com_list = list(combinations(matrix[i][j:j+M], k+1))
                #각 경우의 수 의 합 구하기
                for com_inner in com_list:
                    # 합이 C보다 작으면
                    if sum(com_inner) <= C:
                        com_inner_sum = 0
                        # 각 요소의 제곱의 합을 리스트에 저장
                        for a in com_inner:
                            com_inner_sum += a**2
                        max_sum = max(max_sum, com_inner_sum)
            sum_ij.append([max_sum, i, j])
    sum_ij.sort(reverse=True)
  
    for a in sum_ij:
        for b in sum_ij:
            if a[1] == b[1] and abs(a[2]-b[2]) < M:
                continue
            result = max(result, a[0] + b[0])
    print(f'#{tc} {result}')