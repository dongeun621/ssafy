import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 위치, 숫자
    min = [0, arr[0]]
    max = [0, arr[0]]
 
    for i in range(1, N):
        if min[1] > arr[i]:
            min[0] = i
            min[1] = arr[i]
        if max[1] <= arr[i]:
            max[0] = i
            max[1] = arr[i]
    result = abs(min[0]-max[0])

    print(f'#{test_case} {result}')