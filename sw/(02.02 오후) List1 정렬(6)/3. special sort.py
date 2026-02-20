import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []
 
    arr.sort()
    for i in range(10):
        if i % 2 == 0:
            result.append(arr[(-i//2)-1])
        else:
            result.append(arr[i//2])
    print(f'#{test_case}', end=' ')
    print(*result)