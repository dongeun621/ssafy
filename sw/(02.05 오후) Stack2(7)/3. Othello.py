import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [[0]*N for _ in range(N)]
    z = int(N/2)
    matrix[z][z] = 2
    matrix[z-1][z-1] = 2
    matrix[z-1][z] = 1
    matrix[z][z-1] = 1
 
    dxy = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]
    black = 0
    white = 0
 
    for _ in range(M):
        j, i, k = map(int, input().split())
        i -= 1
        j -= 1
        matrix[i][j] = k
        for a, b in dxy:
            add = []
            ii = i+a
            jj = j+b
            if 0 <= ii < N and 0 <= jj < N:
                while matrix[ii][jj] != k and matrix[ii][jj] != 0:
                    add.append([ii,jj])
                    ii += a
                    jj += b
                    if 0 <= ii < N and 0 <= jj < N:
                        if matrix[ii][jj] == k:
                            for iii, jjj in add:
                                matrix[iii][jjj] = k
                            break
                        elif matrix[ii][jj] == 0:
                            add = []
                            break
 
                    else:
                        add = []
                        break
 
            else: continue
    for i in range(N):
        black += matrix[i].count(1)
        white += matrix[i].count(2)
 
    print(f'#{test_case} {black} {white}')