import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    n = N//2
    result = sum(matrix[n])
    for i in range(1, n+1):
        result += sum(matrix[n+i][i:N-i])
        result += sum(matrix[n-i][i:N-i])
    print(f'#{tc} {result}')