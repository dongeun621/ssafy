import sys

sys.stdin = open('sample_input5.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
 
    print(f'#{test_case}')
 
    for i in range(N):
        result = []
        inner = ''
        for j in range(N-1, -1, -1):
            inner += str(matrix[j][i])
        result.append(inner)
        inner = ''
        for j in range(N-1, -1, -1):
            inner += str(matrix[N-1-i][j])
        result.append(inner)
        inner = ''
        for j in range(0, N):
            inner += str(matrix[j][N-1-i])
        result.append(inner)
        inner = ''
        print(*result)