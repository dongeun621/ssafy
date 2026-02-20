import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    c_list = list(map(int, input().split()))
    result = 1
    max_result = 1
    for i in range(1, N):
        if c_list[i] > c_list[i-1]:
            result += 1
        else:
            max_result = max(max_result, result)
            result = 1
    max_result = max(max_result, result)
    print(f'#{tc} {max_result}')