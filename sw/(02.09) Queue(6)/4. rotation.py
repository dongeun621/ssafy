import sys

sys.stdin = open('sample_input4.txt', 'r')

from collections import deque
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    q = deque(map(int, input().split()))
 
    for _ in range(M):
        q.rotate(-1)
 
 
 
    print(f'#{test_case} {q[0]}')