import sys

sys.stdin = open('sample_input4.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [[] for _ in range(N+1)]

    for i in range(1, N+1):
        data = list(input().split())
        length = len(data)
        if length == 2:
            arr[i] = int(data[1])
        elif length == 4:
            arr[i] = [data[1], int(data[2]), int(data[3])]
    while type(arr[1]) == list:
        for i in range(1, N+1):
            if type(arr[i]) == list and type(arr[arr[i][1]]) == int and type(arr[arr[i][2]]) == int:
                if arr[i][0] == '+':
                    arr[i] = arr[arr[i][1]] + arr[arr[i][2]]
                elif arr[i][0] == '-':
                    arr[i] = arr[arr[i][1]] - arr[arr[i][2]]
                elif arr[i][0] == '*':
                    arr[i] = arr[arr[i][1]] * arr[arr[i][2]]
                elif arr[i][0] == '/':
                    arr[i] = arr[arr[i][1]] // arr[arr[i][2]]
    print(f'#{tc} {arr[1]}')