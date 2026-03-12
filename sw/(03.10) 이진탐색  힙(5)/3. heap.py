import sys

sys.stdin = open('sample_input3.txt', 'r')

from heapq import heappop, heappush

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = []
    result = []

    for _ in range(N):
        a = list(map(int, input().split()))
        if a[0] == 1:
            heappush(heap, -a[1])
        if a[0] == 2:
            if heap:
                result.append(-heappop(heap))
            else:
                result.append(-1)

    print(f'#{tc}', end=' ')
    print(*result)