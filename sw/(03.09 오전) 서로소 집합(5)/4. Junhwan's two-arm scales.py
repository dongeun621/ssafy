import sys

sys.stdin = open('sample_input4.txt', 'r')

import math

fact = [math.factorial(i) for i in range(10)]
pow2 = [2**i for i in range(10)]

def dfs(left, right, visited_sum, cnt):
    global result
    if cnt == arr_cnt:
        result += 1
        return
    if left >= right+arr_sum-visited_sum: #남은 수를 다 오른쪽에 더해도 왼쪽보다 작으면
        result += fact[arr_cnt-cnt]*pow2[arr_cnt-cnt] #남은수의 경우의수 n!*2^n 추가
        return

    for i in range(arr_cnt):
        if visited[i] == 1:
            continue
        next = arr[i]
        visited[i] = 1
        dfs(left+next, right, visited_sum+next, cnt+1)
        if left >= right+next:
            dfs(left, right + next, visited_sum + next, cnt+1)
        visited[i] = 0


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_sum = sum(arr)
    arr_cnt = len(arr)
    visited = [0]*arr_cnt
    result = 0

    dfs(0,0,0,0)


    print(f'#{tc} {result}')
