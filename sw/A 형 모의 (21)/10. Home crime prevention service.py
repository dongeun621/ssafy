import sys

sys.stdin = open('sample_input8.txt', 'r')

from collections import deque
 
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
 
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_cost = sum(sum(i) for i in matrix) * M
    max_house = 0
 
    for i in range(N):
        for j in range(N):
            k = 1
            visited = [[0] * N for _ in range(N)]
            visited[i][j] = 1
            while k * k + (k - 1) ** 2 <= max_cost:
                if k == 1:
                    q = deque([[i, j]])
                    if matrix[i][j] == 1:
                        cnt = 1
                    else:
                        cnt = 0
                else:
                    for _ in range(len(q)):
                        q_pop = q.popleft()
                        for ii, jj in dxy:
                            iii = q_pop[0] + ii
                            jjj = q_pop[1] + jj
                            if 0 <= iii < N and 0 <= jjj < N:
                                if visited[iii][jjj] == 0:
                                    q.append([iii, jjj])
                                    visited[iii][jjj] = 1
                                    if matrix[iii][jjj] == 1:
                                        cnt += 1
 
                if k * k + (k - 1) ** 2 <= cnt * M:
                    max_house = max(max_house, cnt)
                k += 1
    print(f'#{tc} {max_house}')