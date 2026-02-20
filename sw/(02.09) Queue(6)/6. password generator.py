import sys

sys.stdin = open('sample_input6.txt', 'r')

from collections import deque
 
T = 10
for test_case in range(1, T+1):
    t = int(input())
    q = deque(map(int, input().split()))
    cnt = 1
 
    while True:
        q[0] -= cnt
        q.rotate(-1)
        if q[-1] <= 0:
            q[-1] = 0
            break
        if cnt == 5:
            cnt = 1
        else: cnt += 1
 
    print(f'#{test_case}', end=' ')
    print(*q)