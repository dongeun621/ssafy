import sys

sys.stdin = open('sample_input4.txt', 'r')

dxy = [(-1,0), (0,1), (1,0), (0,-1)]

def dfs(i,j,cnt,flag):
    #공사안했으면 공사가능높이까지 깎기가능
    if flag == 0:
        k = K
    else: k = 0
    high = matrix[i][j]
    matrix[i][j] = 100
    for dx, dy in dxy:
        x = i + dx
        y = j + dy
        if 0 <= x < N and 0 <= y < N:
            next_high = matrix[x][y]
            for kk in range(k+1):
                next_flag = flag
                # kk가 1이상이면 무조건 flag = 1
                if kk > 0:
                    next_flag = 1
                # 다음높이가 더 낮아지면 메트릭스 수정 후 dfs실행 후 원복
                if high > next_high - kk:
                    matrix[x][y] -= kk
                    dfs(x,y,cnt+1,next_flag)
                    matrix[x][y] += kk
                    break
    matrix[i][j] = high
    global result
    result = max(result, cnt)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    highest = 0
    highest_list = []
    result = 0
    #최고높이 찾기
    for i in range(N):
        for j in range(N):
            highest = max(highest, matrix[i][j])
    #최고높이인 좌표찾기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == highest:
                highest_list.append((i,j))

    for i,j in highest_list:
        dfs(i, j, 1, 0)

    print(f'#{tc} {result}')