import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, num = input().split()
    N = int(N)
    num = list(num)
    arr = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    new_num = []
    for i in num[::-1]:
        if '0' <= i <= '9':
            i = int(i)
        else: i = arr[i]

        for _ in range(4):
            new_num.append(i%2)
            i //= 2
    binary_str = ''.join(map(str, new_num[::-1]))
    print(f'#{tc} {binary_str}')