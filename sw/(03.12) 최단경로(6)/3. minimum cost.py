import sys

sys.stdin = open('sample_input3.txt', 'r')

from heapq import heappop, heappush

dxy = [(-1,0), (0,1), (1,0), (0,-1)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    min_cost = [[float('inf')]*N for _ in range(N)]
    min_cost[0][0] = 0
    heap = [(0, matrix[0][0], 0, 0)]

    while heap:
        before_cost, before_height, i, j = heappop(heap)
        for dx, dy in dxy:
            x = i + dx
            y = j + dy
            if 0 <= x < N and 0 <= y < N:
                after = matrix[x][y]
                if before_height >= after:
                    high_d = 1
                else:
                    high_d = after - before_height + 1
                next_cost = before_cost + high_d
                if min_cost[x][y] > next_cost:
                    min_cost[x][y] = next_cost
                    heappush(heap, (next_cost, matrix[x][y], x, y))


    print(f'#{tc} {min_cost[N-1][N-1]}')