import sys

sys.stdin = open('sample_input9.txt', 'r')

T = 10
for tc in range(1, T+1):
    N, arr = input().split()
    arr = list(arr)
    stack = []
    for i in arr:
        if stack:
            if stack[-1] == i:
                stack.pop()
                continue
        stack.append(i)
 
    print(f'#{tc} ', end='')
    print(*stack, sep='')