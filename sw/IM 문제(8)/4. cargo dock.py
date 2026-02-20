import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    n_list = [list(map(int, input().split())) for _ in range(N)]
    n_list.sort(key=lambda x: x[1])
    result = 0
    time = 0
    for s, e in n_list:
        if time <= s:
            result += 1
            time = e
    print(f'#{tc} {result}')