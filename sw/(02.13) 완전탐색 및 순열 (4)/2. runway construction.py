import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            a = matrix[i][j-1]
            b = matrix[i][j]
            if a == b:
                cnt += 1
                continue
            elif a - b == 1:
                if j <= N-X and cnt >= 0:
                    cnt = 1-X
                    continue
                else:
                    result -= 1
                    break
            elif a - b == -1:
                if cnt >= X:
                    cnt = 1
                    continue
                else:
                    result -= 1
                    break
            else:
                result -= 1
                break
        result += 1
        cnt = 1
        for j in range(1, N):
            a = matrix[j-1][i]
            b = matrix[j][i]
            if a == b:
                cnt += 1
                continue
            elif a - b == 1:
                if j <= N-X and cnt >= 0:
                    cnt = 1-X
                    continue
                else:
                    result -= 1
                    break
            elif a - b == -1:
                if cnt >= X:
                    cnt = 1
                    continue
                else:
                    result -= 1
                    break
            else:
                result -= 1
                break
        result += 1
    print(f'#{tc} {result}')