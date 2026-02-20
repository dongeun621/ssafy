import sys

sys.stdin = open('sample_input7.txt', 'r')

from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    if N % 2 == 0:
        a = int(N/2)
    else:
        a = N//2 + 1
    arr1 = deque(arr[:a])
    arr2 = deque(arr[a:])
    result = []
    for i in range(a):
        result.append(arr1.popleft())
        if arr2:
            result.append(arr2.popleft())
 
    print(f'#{tc}', end=' ')
    print(*result)