import sys

sys.stdin = open('in.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    M = max(arr)
    maxgap = 0
    for i in range(1, M+1):
        boxlist = []
        gap = 0
        for j in range(N):
            if arr[j] >= i:
                boxlist.append(j)
        gap = N-boxlist[0]-len(boxlist)
        if maxgap < gap:
            maxgap = gap
    print(f'#{test_case} {maxgap}')