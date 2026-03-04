import sys

sys.stdin = open('sample_input4.txt', 'r')

dxy = [[-1,0], [0,1], [1,0], [0,-1]]

for _ in range(10):
    tc = int(input())
    matrix = [list(input()) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    stack = []
    result = 0
    for i in range(16):
        for j in range(16):
            matrix[i][j] = int(matrix[i][j])
            if matrix[i][j] == 2:
                stack.append([i,j])


    while stack and result == 0:
        i,j = stack.pop()
        visited[i][j] = 1
        for x,y in dxy:
            ii = i + x
            jj = j + y
            if 0 <= ii < 16 and 0 <= jj < 16 and visited[ii][jj] == 0:
                if matrix[ii][jj] == 0:
                    stack.append([ii,jj])
                elif matrix[ii][jj] == 3:
                    result = 1
    print(f'#{tc} {result}')


