import sys

sys.stdin = open('sample_input4.txt', 'r')

from collections import deque
dxy = [(-1,0), (0,1), (1,0), (0,-1)]

for _ in range(10):
    tc = int(input())
    N = 16
    matrix_temp = [list(input()) for _ in range(N)]
    matrix = [[0]*N for _ in range(N)]
    q = deque()
    result = 0

    for i in range(N):
        for j in range(N):
            matrix[i][j] = int(matrix_temp[i][j])

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                q.append((i,j))
                break
        if q:
            break

    while q:
        ii,jj = q.popleft()
        for dx, dy in dxy:
            x = ii+dx
            y = jj+dy
            if 0 <= x < N and 0 <= y < N:
                if matrix[x][y] == 0:
                    matrix[x][y] = 2
                    q.append((x,y))
                elif matrix[x][y] == 3:
                    result = 1
                    break

    print(f'#{tc} {result}')