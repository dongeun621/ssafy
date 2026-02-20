import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 1
    m = 1
    for i in range(1, N):
        if arr[i] > arr[i-1]:
            m += 1
        else:
            result = max(result, m)
            m = 1
        if i == N-1:
            result = max(result, m)
    print(f'#{tc} {result}')