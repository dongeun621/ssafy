import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_list = []
    for i in range(N-M+1):
        sum_list.append(sum(arr[i:i+M]))
    sum_list.sort()
    result = sum_list[-1]-sum_list[0]
    print(f'#{test_case} {result}')