import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, X= map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 1
        updown = 0
        for j in range(1, N):
            if abs(matrix[i][j-1] - matrix[i][j]) > 1:
                break
            if matrix[i][j-1] == matrix[i][j]:
                cnt += 1
            elif matrix[i][j-1] >= matrix[i][j]:
                if updown == -1 and cnt < X:
                    break
                elif N < j+X:
                    break
                updown = -1
                cnt = 1
            elif matrix[i][j-1] <= matrix[i][j]:
                if updown == 0 and cnt < X:
                    break
                elif updown == 1 and cnt < X:
                    break
                elif updown == -1 and cnt < X*2:
                    break
                updown = 1
                cnt = 1
            if j == N-1:
                result += 1
        cnt = 1
        updown = 0
        for j in range(1, N):
            if abs(matrix[j-1][i] - matrix[j][i]) > 1:
                break
            if matrix[j-1][i] == matrix[j][i]:
                cnt += 1
            elif matrix[j-1][i] >= matrix[j][i]:
                if updown == -1 and cnt < X:
                    break
                elif N < j+X:
                    break
                updown = -1
                cnt = 1
            elif matrix[j-1][i] <= matrix[j][i]:
                if updown == 0 and cnt < X:
                    break
                elif updown == 1 and cnt < X:
                    break
                elif updown == -1 and cnt < X*2:
                    break
                updown = 1
                cnt = 1
            if j == N-1:
                result += 1
    print(f'#{test_case} {result}')