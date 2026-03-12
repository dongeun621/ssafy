import sys

sys.stdin = open('sample_input5.txt', 'r')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = deque(map(int, input().split()))
    B = list(map(int, input().split()))
    a = len(A)
    b = len(B)
    result = 0
    direct = 1

    if a > b:
        direct = -1
        cnt = 0
        while a > b + cnt:
            cnt += 1
            B.append(0)

    elif b > a:
        cnt = 0
        while b > a + cnt:
            cnt += 1
            A.append(0)

    for _ in range(abs(a-b)+1):
        sum_i = 0
        for i in range(max(a,b)):
            sum_i += A[i]*B[i]
        result = max(result, sum_i)
        A.rotate(direct)

    print(f'#{tc} {result}')