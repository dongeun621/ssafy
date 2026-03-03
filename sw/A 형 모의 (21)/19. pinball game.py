import sys

sys.stdin = open('sample_input19.txt', 'r')

dxy = [[-1,0], [0,1], [1,0], [0,-1]]
block_dxy = [[2,3,0,1], [2,3,1,0], [1,3,0,2], [3,2,0,1], [2,0,3,1], [2,3,0,1]]

def shoot(direct, start_i, start_j):
    cnt = 0
    current_i = start_i
    current_j = start_j
    while True:
        current_i += dxy[direct][0]
        current_j += dxy[direct][1]
        if current_i < 0 or current_i >= N or current_j < 0 or current_j >= N: #벽만나면
            direct = block_dxy[0][direct]
            cnt += 1
            continue
        else:
            a = matrix[current_i][current_j]

        if current_i == start_i and current_j == start_j: #시작점으로 돌아오면
            return cnt
        elif a == 0:
            continue
        elif a == -1: #블랙홀이면
            return cnt
        elif a > 5: #화이트홀이면
            if white[a][0] == [current_i,current_j]:
                current_i, current_j = white[a][1]
            else:
                current_i, current_j = white[a][0]
        elif 0 < a < 6:
            direct = block_dxy[a][direct]
            cnt += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    white = {6:[], 7:[], 8:[], 9:[], 10:[]}
    result = 0
    for i in range(N):
        for j in range(N):
            if 6 <= matrix[i][j] <= 10:
                white[matrix[i][j]].append([i,j])

    for i in range(N):
        for j in range(N):
            for k in range(4):
                if matrix[i][j] == 0:
                    cnt = shoot(k, i, j)
                    result = max(result, cnt)

    print(f'#{tc} {result}')