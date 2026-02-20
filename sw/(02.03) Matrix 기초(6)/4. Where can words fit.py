import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    result = 0
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix.append([0]*N)
    [matrix[i].append(0) for i in range(N+1)]
    for i in range(N):
        for j in range(N-K+1):
            if matrix[i][j] == 1 and matrix[i][j-1] == 0:
                for k in range(1, K+1):
                    if k < K and matrix[i][j+k] == 0:
                        break
                    if k == K and matrix[i][j+k] == 0:
                        result += 1
    for i in range(N):
        for j in range(N-K+1):
            if matrix[j][i] == 1 and matrix[j-1][i] == 0:
                for k in range(1, K+1):
                    if k < K and matrix[j+k][i] == 0:
                        break
                    if k == K and matrix[j+k][i] == 0:
                        result += 1
 
    print(f'#{test_case} {result}')