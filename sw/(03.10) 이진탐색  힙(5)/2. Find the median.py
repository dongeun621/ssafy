import sys

sys.stdin = open('sample_input2.txt', 'r')

from heapq import heappop, heappush

T = int(input())
for tc in range(1, T+1):
    N, A = map(int, input().split())
    min_heap = [A]
    max_heap = []
    result = 0

    for _ in range(N):
        middle = min_heap[0]
        a, b = map(int, input().split())

        if a > middle:
            heappush(min_heap, a)
            if b > middle:
                heappush(min_heap, b)
                heappush(max_heap, -heappop(min_heap))
            else:
                heappush(max_heap, -b)
        elif a < middle:
            heappush(max_heap, -a)
            if b < middle:
                heappush(max_heap, -b)
                heappush(min_heap, -heappop(max_heap))
            else:
                heappush(min_heap, b)
        elif a == middle:
            if b > middle:
                heappush(min_heap, b)
                heappush(max_heap, -a)
            else:
                heappush(min_heap, a)
                heappush(max_heap, -b)

        result += min_heap[0]
    result %= 20171109
    print(f'#{tc} {result}')