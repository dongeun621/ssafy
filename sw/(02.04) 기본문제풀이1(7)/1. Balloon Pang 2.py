import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_s = 0
    dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in range(N):
        for j in range(M):
            s = matrix[i][j]
            for dx, dy in dxy:
                if 0 <= i+dx < N and 0 <= j+dy < M:
                    s += matrix[i+dx][j+dy]
 
            max_s = max(max_s, s)
    print(f'#{test_case} {max_s}')