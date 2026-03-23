import sys

sys.stdin = open('sample_input6.txt', 'r')

from heapq import heappop, heappush

dxy = [(-1,0), (0,1), (1,0), (0,-1)]

T =  int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    visited = [[float('inf')]*N for _ in range(N)]

    heap = [(0,0,0)]

    while heap:
        d, i, j = heappop(heap)
        if visited[i][j] <= d:
            continue
        visited[i][j] = d
        for dx, dy in dxy:
            x = i+dx
            y = j+dy
            if 0 <= x < N and 0 <= y < N:
                next_d = int(matrix[x][y])
                if visited[x][y] > d+next_d:
                    heappush(heap, (d+next_d, x, y))

    print(f'#{tc} {visited[-1][-1]}')