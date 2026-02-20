import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            if matrix[i][j:j+M] == matrix[i][j:j+M][::-1]:
                print(f'#{test_case}', end=' ')
                print(*matrix[i][j:j+M], sep='')
                break
 
    for i in range(N):
        word = []
        for j in range(N):
            word.append(matrix[j][i])
        for j in range(N-M+1):
            if word[j:j+M] == word[j:j+M][::-1]:
                print(f'#{test_case}', end=' ')
                print(*word[j:j+M], sep='')