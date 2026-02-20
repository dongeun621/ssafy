import sys

sys.stdin = open('sample_input5.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    m = 0
    result = 0
 
    for i in range(N-1,-1, -1):
        if m < arr[i]:
            m = arr[i]
        else:
            result += m - arr[i]
 
    print(f'#{test_case} {result}')