import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    result = 'NO'
    dxy = [[1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1], [0,1]]
 
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'o':
                for ii, jj in dxy:
                    for k in range(5):
                        a = i+ii*k
                        b = j+jj*k
                        if 0 <= a < N and 0 <= b < N:
                            if matrix[a][b] != 'o':
                                break
                            elif k == 4:
                                result = 'YES'
 
    print(f'#{test_case} {result}')