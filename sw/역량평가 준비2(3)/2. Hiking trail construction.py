import sys

sys.stdin = open('sample_input2.txt', 'r')

dxy = [[-1,0], [0,1], [1,0], [0,-1]]

def research(height,x,y,cnt,plag,visited):
    if plag == 1:
        k = 1 #이미깎았으면 이제 안깎음
    else: k = 1+K #아직안깎았으면 깎아도 됨
    visited.append([x,y])
    for dx, dy in dxy: #방향
        xx = x + dx  # 좌표 먼저 구하고
        yy = y + dy
        if 0 <= xx < N and 0 <= yy < N and [xx,yy] not in visited:  # matrix 안인지 확인
            for kk in range(k): #깎을높이
                next_high = matrix[xx][yy] - kk #높이 구하고
                if height > next_high: #다음 높이가 더 낮고
                    if kk == 0 and plag == 0: #아직 안 깎은 경우
                        research(next_high, xx, yy, cnt+1, 0, visited[:])
                    else: #이미 깎은 경우
                        research(next_high, xx, yy, cnt+1, 1, visited[:])
    global result
    result = max(result, cnt)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    highest = 0
    result = 0
    for i in range(N):
        for j in range(N):
            highest = max(highest, matrix[i][j])

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == highest:
                research(highest,i,j,1,0,[])

    print(f'#{tc} {result}')