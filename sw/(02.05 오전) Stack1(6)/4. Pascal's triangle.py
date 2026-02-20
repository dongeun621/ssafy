import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print(f'#{test_case}')
    arr = [1]
    print(*arr)
    for i in range(N-1):
        result = [1]
        for j in range(len(arr)):
            if j == len(arr)-1:
                result.append(1)
            else:
                result.append(arr[j]+arr[j+1])
        arr = result
        print(*result)