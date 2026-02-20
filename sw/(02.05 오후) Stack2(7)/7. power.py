import sys

sys.stdin = open('sample_input7.txt', 'r')

def a(n, i, m):
    if m == 1:
        return i
    return a(n, i*n, m-1)
 
T = 10
for test_case in range(1, T+1):
    t = input()
    N, M = map(int, input().split())
    result = 0
 
    result = a(N, N, M)
 
    print(f'#{test_case} {result}')