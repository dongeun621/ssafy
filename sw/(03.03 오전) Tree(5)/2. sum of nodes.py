import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+1)

    for _ in range(M):
        data = list(map(int, input().split()))
        arr[data[0]] = data[1]
    for i in range(N, 0, -1):
        arr[i//2] += arr[i]

    print(f'#{tc} {arr[L]}')