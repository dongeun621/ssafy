import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum1 = 0
            for a in range(M):
                for b in range(M):
                    sum1 += matrix[i+a][j+b]
            if result < sum1:
                result = sum1
 
 
    print(f'#{test_case} {result}')