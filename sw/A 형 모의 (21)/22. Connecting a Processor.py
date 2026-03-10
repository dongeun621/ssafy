import sys

sys.stdin = open('sample_input22.txt', 'r')

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def change(x,y,dx,dy,k,value):
    for _ in range(k):
        x += dx
        y += dy
        matrix[x][y] = value

def comfirm(x,y,dx,dy):
    cnt = 0
    while True:
        x += dx
        y += dy
        if 0 <= x < N and 0 <= y < N:
            if matrix[x][y] != 0:
                return False
            cnt += 1
        else:
            break

    return cnt

def dfs(idx, cnt, cost):
    global max_core, min_cost
    #가지치기
    if cores_cnt - idx + cnt < max_core: #남은 코어수 + 연결된 코어수가 최대코어수보다 작으면 끝
        return
    #결과처리
    if idx == cores_cnt:#모든코어 탐색 했으면
        max_core = max(max_core, cnt)
        min_cost[cnt-1] = min(min_cost[cnt-1], cost)
        return
    for core_idx in range(idx, cores_cnt):
        x,y = cores[core_idx]
        for dx, dy in dxy:
            d_cost = comfirm(x,y,dx,dy)
            if d_cost != False:
                change(x,y,dx,dy,d_cost,2)
                dfs(core_idx+1, cnt+1, cost+d_cost)
                change(x,y,dx,dy,d_cost,0)

        dfs(core_idx+1, cnt, cost)




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    cores = []
    result = 0

    for i in range(1, N-1):
        for j in range(1, N-1):
            if matrix[i][j] == 1:
                cores.append((i,j))
    cores_cnt = len(cores)
    max_core = 0
    min_cost = [float('inf') for _ in range(len(cores))]

    if cores:
        dfs(0,0,0)

    result = min_cost[max_core-1]
    print(f'#{tc} {result}')

