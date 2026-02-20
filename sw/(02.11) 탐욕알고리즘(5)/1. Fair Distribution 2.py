import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    candy = list(map(int, input().split()))
    candy.sort()
    m = 10**9
    for i in range(N-K+1):
        delta = candy[K+i-1] - candy[i]
        m = min(m, delta)
 
    print(f'#{test_case} {m}')