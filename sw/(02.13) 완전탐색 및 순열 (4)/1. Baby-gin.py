import sys

sys.stdin = open('sample_input1.txt', 'r')

from itertools import combinations, permutations
T = int(input())
for tc in range(1, 1+T):
    arr1 = list(input().strip())
    arr = []
    index = set([0,1,2,3,4,5])
    result = 'false'
    for i in arr1:
        arr.append(int(i))
    arr.sort()
    for i in combinations(index, 3):
        i_rev = list(index - set(i))
        i = list(i)
        i = sorted(i)
        i_rev = sorted(i_rev)
        first = 0
        second = 0
        for ii in range(1,3):
            if arr[i[ii]]-arr[i[ii-1]] != 1:
                break
            elif ii == 2:
                first = 1
        if first == 0:
            for ii in range(1,3):
                if arr[i[ii]] != arr[i[ii-1]]:
                    break
                elif ii == 2:
                    first = 1
        if first == 0:
            continue
        for ii in range(1,3):
            if arr[i_rev[ii]]-arr[i_rev[ii-1]] != 1:
                break
            elif ii == 2:
                second = 1
        if second == 0:
            for ii in range(1,3):
                if arr[i_rev[ii]] != arr[i_rev[ii-1]]:
                    break
                elif ii == 2:
                    second = 1
        if second == 1:
            result = 'true'
            break


    print(f'#{tc} {result}')