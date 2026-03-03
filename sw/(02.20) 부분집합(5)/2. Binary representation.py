import sys

sys.stdin = open('sample_input2.txt', 'r')

from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = deque()
    result = 'ON'
    if M == 0:
        arr.append(0)
    for _ in range(N):
        if M % 2 == 1:
            M //= 2
        else:
            result = 'OFF'
            break
    print(f'#{tc} {result}')