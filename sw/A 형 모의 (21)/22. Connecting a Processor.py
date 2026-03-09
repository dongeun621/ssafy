import sys

sys.stdin = open('sample_input22.txt', 'r')

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def can_connect(x, y, dx, dy):
    nx, ny = x + dx, y + dy
    while 0 <= nx < N and 0 <= ny < N:
        if matrix[nx][ny] != 0:
            return False
        nx += dx
        ny += dy
    return True

def set_line(x, y, dx, dy, value):
    nx, ny = x + dx, y + dy
    length = 0
    while 0 <= nx < N and 0 <= ny < N:
        matrix[nx][ny] = value
        length += 1
        nx += dx
        ny += dy
    return length

def dfs(idx, connected_cnt, cost):
    global best_core, best_len

    # 가지치기: 남은 코어를 전부 연결해도 최고 기록 불가
    if connected_cnt + (len(cores) - idx) < best_core:
        return

    if idx == len(cores):
        if connected_cnt > best_core:
            best_core = connected_cnt
            best_len = cost
        elif connected_cnt == best_core:
            best_len = min(best_len, cost)
        return

    x, y = cores[idx]

    # 4방향 연결 시도
    for dx, dy in dxy:
        if can_connect(x, y, dx, dy):
            line_len = set_line(x, y, dx, dy, 2)
            dfs(idx + 1, connected_cnt + 1, cost + line_len)
            set_line(x, y, dx, dy, 0)

    # 연결하지 않는 경우
    dfs(idx + 1, connected_cnt, cost)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    cores = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if matrix[i][j] == 1:
                cores.append((i, j))

    best_core = -1
    best_len = float('inf')

    dfs(0, 0, 0)

    print(f'#{tc} {best_len}')
