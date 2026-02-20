import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [[0]*10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        color = list(map(int, input().split()))
        for i in range(color[0],color[2]+1):
            for j in range(color[1],color[3]+1):
                if color[4] == 1 and matrix[i][j] != 2:
                    matrix[i][j] = 1
                elif color[4] == 1 and matrix[i][j] == 2:
                    matrix[i][j] = 3
                    cnt += 1
                elif color[4] == 2 and matrix[i][j] != 1:
                    matrix[i][j] = 2
                elif color[4] == 2 and matrix[i][j] == 1:
                    matrix[i][j] = 3
                    cnt += 1
 
    print(f'#{test_case} {cnt}')