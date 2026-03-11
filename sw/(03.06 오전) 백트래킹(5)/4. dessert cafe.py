import sys

sys.stdin = open('sample_input4.txt', 'r')

dx = [1,1,-1,-1]
dy = [1,-1,-1,1]

def dfs(i,j,start_i,start_j,cnt,direct):
    #결과반영조건
    if i == start_i and j == start_j and direct == 3:
        global result
        result = max(result, cnt)
    if desert_num[matrix[i][j]] == 1:  # 벽에닿거나, 먹은 디저트면 안함
        return
    #디저트 추가
    desert_num[matrix[i][j]] = 1
    for idx in range(direct, min(direct+2,4)):
        x = i+dx[idx]
        y = j+dy[idx]
        if 0 <= x < N and 0 <= y < N:
            dfs(x,y,start_i,start_j,cnt+1,idx)
    #디저트 빼기
    desert_num[matrix[i][j]] = 0


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    result = -1
    desert_num = [0]*101

    for i in range(N-2):
        for j in range(1, N-1):
            dfs(i,j,i,j,0,0)

    print(f'#{tc} {result}')