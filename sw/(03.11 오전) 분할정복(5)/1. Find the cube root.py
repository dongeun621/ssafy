import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = 0
    while True:
        x += 1
        if x**3 == N:
            break
        if x**3 > N:
            x = -1
            break
    print(f'#{tc} {x}')