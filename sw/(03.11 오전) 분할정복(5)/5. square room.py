import sys

sys.stdin = open('sample_input5.txt', 'r')

dxy = [(-1,0), (0,1), (1,0), (0,-1)]

def dfs(i,j,cnt):
    before = matrix[i][j]
    for dx, dy in dxy:
        x = i + dx
        y = j + dy
        if 0 <= x < N and 0 <= y < N and before+1 == matrix[x][y]:
            dfs(x,y,cnt+1)

    global result
    result = max(result, cnt)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    room_num = float('inf')

    for i in range(N):
        for j in range(N):
            room = matrix[i][j]
            stack = [(i,j,1)]
            while stack:
                i, j, cnt = stack.pop()
                before = matrix[i][j]
                for dx, dy in dxy:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < N and 0 <= y < N and before + 1 == matrix[x][y]:
                        stack.append((x, y, cnt + 1))
                if cnt == result:
                    room_num = min(room_num, room)
                elif cnt >= result:
                    result = cnt
                    room_num = room


            if result == N**2:
                break
        if result == N ** 2:
            break

    print(f'#{tc} {room_num} {result}')