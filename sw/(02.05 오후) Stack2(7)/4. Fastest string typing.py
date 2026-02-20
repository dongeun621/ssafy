import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    A, B = input().split()
    k = len(B)
    stack = []
    result = len(A)
    for a in A:
        stack.append(a)
        if len(stack) >= k:
            if stack[len(stack)-k:] == list(B):
                result -= k-1
                for _ in range(k):
                    stack.pop()
    print(f'#{test_case} {result}')