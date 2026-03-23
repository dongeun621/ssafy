import sys

sys.stdin = open('sample_input4.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    A_len = len(A)
    B_len = len(B)
    i = 0
    result = 0
    while i < A_len:
        result += 1
        if A[i:i+B_len] == B:
            i += B_len
        else: i += 1

    print(f'#{tc} {result}')