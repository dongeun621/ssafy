import sys

sys.stdin = open('sample_input1.txt', 'r')

dxy = [[-1,0], [0,1], [1,0], [0,-1]]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dij_matrix = [[99999]*N for _ in range(N)]
    dij_matrix[0][0] = 0
    visited = [[0]*N for _ in range(N)]
    while visited[N-1][N-1] == 0:
        min_idx = [0,0,99999]
        # 최소 dij 찾기
        for i in range(N):
            for j in range(N):
                if dij_matrix[i][j] < min_idx[2] and visited[i][j] == 0:
                    min_idx = [i,j,dij_matrix[i][j]]

        # 최소 dij에서 dxy 탐색
        i = min_idx[0]
        j = min_idx[1]
        visited[i][j] = 1
        for dx, dy in dxy:
            x = i + dx
            y = j + dy
            if 0 <= x < N and 0 <= y < N:
                before = matrix[i][j]
                after = matrix[x][y]
                if before == after:
                    distance = 1
                elif before > after:
                    distance = 0
                elif before < after:
                    distance = (after-before)*2
                dij_matrix[x][y] = min(dij_matrix[x][y], dij_matrix[i][j] + distance)


    print(f'#{tc} {dij_matrix[N-1][N-1]}')