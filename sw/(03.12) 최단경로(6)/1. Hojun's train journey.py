import sys

sys.stdin = open('sample_input1.txt', 'r')

from heapq import heappop, heappush

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N)]

    for a, b, cost in arr:
        graph[a].append((cost,b))

    heap = [(0,0)]
    dist = [float('inf')] * N

    while heap:
        cost, node = heappop(heap)
        if dist[node] <= cost: #기존 거리가 더 짧거나 같으면 continue
            continue

        dist[node] = cost #거리 최신화
        for d, next_node in graph[node]: #다음노드 탐색
            if dist[next_node] > d + cost: #다음노드까지의 기존거리보다 짧을때만 추가
                heappush(heap, (d + cost, next_node))
    if dist[-1] == float('inf'):
        dist[-1] = 'impossible'

    print(f'#{tc} {dist[-1]}')