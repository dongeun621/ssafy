import sys

sys.stdin = open('sample_input2.txt', 'r')

from collections import deque
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    cost = [int(input()) for _ in range(N)]
    weight = [int(input()) for _ in range(M)]
    wait = deque()
    park = [0]*N
    result = 0
 
    for i in range(M*2):
        a = int(input())
        if a > 0:
            for i in range(N):
                if park[i] == 0:
                    park[i] = a
                    result += weight[a-1]*cost[i]
                    break
                if i == N-1:
                    wait.append(a)
        elif a < 0:
            a = -a
            for i in range(N):
                if park[i] == a:
                    park[i] = 0
                    if wait:
                        b = wait.popleft()
                        park[i] = b
                        result += weight[b-1]*cost[i]
                    break
 
 
 
 
    print(f'#{test_case} {result}')