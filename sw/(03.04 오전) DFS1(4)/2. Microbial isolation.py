import sys

sys.stdin = open('sample_input2.txt', 'r')

import copy
dxy = [0, [-1,0], [1,0], [0,-1], [0,1]]
dxy_reserve = [0, 2, 1, 4, 3]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = {}
    for _ in range(K):
        data = list(map(int, input().split()))
        arr[(data[0], data[1])] = [data[2], data[2], data[3]]
    for _ in range(M):
        arr_temp = {}
        for (i,j), [s,m,d] in arr.items():
            i += dxy[d][0]
            j += dxy[d][1]

            if i == 0 or i == N-1 or j == 0 or j == N-1:
                d = dxy_reserve[d]
                s //= 2
                if s == 0:
                    continue
            m = s
            if (i,j) in arr_temp:
                if m > arr_temp[(i, j)][1]:
                    arr_temp[(i, j)][1] = m
                    arr_temp[(i, j)][2] = d
                arr_temp[(i, j)][0] += s
            else:
                arr_temp[(i, j)] = [s,m,d]

        arr = copy.deepcopy(arr_temp)
    result = 0
    for s,m,d in arr.values():
        result += s

    print(f'#{tc} {result}')