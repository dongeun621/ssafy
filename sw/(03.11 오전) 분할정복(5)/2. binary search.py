import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    result = 0

    for b in B:
        l = 0
        r = N-1
        before_d = 0
        while True:
            m = (l+r)//2
            v = A[m]
            if b == v:
                result += 1
                break
            elif b < v:
                if before_d == -1:
                    break
                before_d = -1
                r = m-1
            elif b > v:
                if before_d == 1:
                    break
                before_d = 1
                l = m+1

    print(f'#{tc} {result}')