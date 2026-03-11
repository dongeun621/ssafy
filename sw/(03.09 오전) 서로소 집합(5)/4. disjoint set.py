import sys

sys.stdin = open('sample_input4.txt', 'r')

def dfs(left, right, cnt):
    if right > left:
        return
    if cnt == N:
        global result
        result += 1
    for i, a in enumerate(arr):
        if visited[i] == 0:
            visited[i] = 1
            if cnt != 0:
                dfs(left, right + a, cnt + 1)
            dfs(left+a, right, cnt+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    visited = [0]*N

    dfs(0,0,0)

    print(f'#{tc} {result}')
