import sys

sys.stdin = open('sample_input6.txt', 'r')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(8)]
    result = 0
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            word = []
            for k in range(N):
                word.append(matrix[i][j+k])
            if word == word[::-1]:
                result += 1
 
            word = []
            for k in range(N):
                word.append(matrix[j+k][i])
            if word == word[::-1]:
                result += 1
    print(f'#{test_case} {result}')