import sys

sys.stdin = open('sample_input4.txt', 'r')

from heapq import heappop, heappush

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    min_cost_all = [0]*(N+1)
    result = [0]*(N+1)
    for _ in range(M):
        x, y, c = map(int, input().split())
        heappush(graph[x],(c,y))
    for i in range(1, N+1):
        min_cost = [float('inf')]*(N+1)
        min_cost[i] = 0
        heap = [(c,y) for c, y in graph[i]]
        while heap:
            cost, n = heappop(heap)
            if min_cost[n] <= cost:
                continue
            min_cost[n] = cost
            for c, y in graph[n]:
                if min_cost[y] > cost + c:
                    heappush(heap, (cost+c, y))
        min_cost_all[i] = min_cost
    for i in range(1, N+1):
        if i == X:
            continue
        result[i] = min_cost_all[i][X]+min_cost_all[X][i]

    print(f'#{tc} {max(result)}')