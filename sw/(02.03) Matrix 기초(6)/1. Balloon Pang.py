import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
 
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    max = 0
 
    for i in range(N):
        for j in range(M):
            sum = matrix[i][j]
            for k in range(4):
                for l in range(1, matrix[i][j]+1):
                    if i + dx[k]*l > N-1 or i + dx[k]*l < 0 or j + dy[k]*l > M-1 or j + dy[k]*l <0:
                        continue
                    sum += matrix[i + dx[k]*l][j + dy[k]*l]
 
            if max < sum:
                max = sum
    print(f'#{test_case} {max}')