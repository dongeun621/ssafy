import sys

sys.stdin = open('sample_input3.txt', 'r')

dxy = [[-1,0], [0,1], [1,0], [0,-1]]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_cost = sum(sum(matrix[i]) for i in range(N))*M
    result = 0
    for i in range(N):
        for j in range(N):
            cost = 1
            cost_dp = 4
            cnt = 0
            stack = [[i,j]]
            visited = [[0]*N for _ in range(N)]
            visited[i][j] = 1
            while True:
                stack_temp = []
                while stack:
                    x, y = stack.pop()
                    if matrix[x][y] == 1:
                        cnt += 1
                    for dx, dy in dxy:
                        xx = x+dx
                        yy = y+dy
                        if 0 <= xx < N and 0 <= yy < N and visited[xx][yy] == 0:
                            visited[xx][yy] = 1
                            stack_temp.append([xx,yy])
                if cnt * M >= cost:
                    result = max(result, cnt)
                cost += cost_dp
                cost_dp += 4
                if cost > max_cost:
                    break
                stack = stack_temp



    print(f'#{tc} {result}')