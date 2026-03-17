import sys

sys.stdin = open('sample_input4.txt', 'r')

from heapq import heappop, heappush

T = int(input())
for tc in range(1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        heappush(graph[x],(c,y))

    for i in range(1, N+1):
        if i == X:
            continue

        min_cost = [float('inf')]*(N+1)
        min_cost[i] = 0
        heap = [(0,c,y) for c, y in graph[i]]

        while heap:
            before_cost, cost, n = heappop(heap)
            for c, y in graph[n]: