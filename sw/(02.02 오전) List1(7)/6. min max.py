import sys

sys.stdin = open('sample_input6.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    min = arr[0]
    max = arr[0]
    for i in arr:
        if min > i:
            min = i
        if max < i:
            max = i
    result = max-min
    print(f'#{test_case} {result}')