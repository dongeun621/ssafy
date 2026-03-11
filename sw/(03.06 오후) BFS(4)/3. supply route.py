import sys

sys.stdin = open('sample_input3.txt', 'r')

from heapq import heappop, heappush

dxy = [(-1,0), (0,1), (1,0), (0,-1)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix_temp = [list(input()) for _ in range(N)]
    matrix = [[0]*N for _ in range(N)]
    visited = [[float('inf')]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            matrix[i][j] = int(matrix_temp[i][j])

    hp = []
    heappush(hp, (0,0,0))

    while hp:
        cost, i, j = heappop(hp)
        for dx, dy in dxy:
            x = i+dx
            y = j+dy

            if 0 <= x < N and 0 <= y < N:
                next_cost = cost + matrix[x][y]
                if visited[x][y] > next_cost:
                    visited[x][y] = next_cost
                    heappush(hp, (next_cost, x, y))

    print(f'#{tc} {visited[N - 1][N - 1]}')
