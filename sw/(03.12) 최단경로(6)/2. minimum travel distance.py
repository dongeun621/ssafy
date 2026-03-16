import sys

sys.stdin = open('sample_input2.txt', 'r')

from heapq import heappush, heappop

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dist = [float('inf')]*(N+1)
    for _ in range(E):
        a, b, cost = map(int, input().split())
        graph[a].append((cost, b))

    heap = [(0,0)]
    while heap:
        cost, i = heappop(heap)
        if dist[i] <= cost:
            continue
        dist[i] = cost
        for next_cost, next_i in graph[i]:
            if dist[next_i] > cost + next_cost:
                heappush(heap, (cost+next_cost, next_i))

    print(f'#{tc} {dist[-1]}')