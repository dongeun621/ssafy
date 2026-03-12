import sys

sys.stdin = open('sample_input1.txt', 'r')

dxy = [(-1,0), (0,1), (1,0), (0,-1)]

def gravity():
    global matrix
    cnt = 0
    temp = [[0]*W for _ in range(H)]
    for j in range(W):
        next_h = -1
        for i in range(H-1,-1,-1):
            k = matrix[i][j]
            if k != 0:
                temp[next_h][j] = k
                next_h -= 1
                cnt += 1
    matrix = temp.copy()
    return cnt

def dfs(i,j):
    stack = [(i,j)]
    while stack:
        i, j = stack.pop()
        k = matrix[i][j]
        matrix[i][j] = 0
        if k > 1:
            for dx, dy in dxy:
                for kk in range(1,k):
                    x = i + dx*kk
                    y = j + dy*kk
                    if 0 <= x < H and 0 <= y < W and matrix[x][y] != 0:
                        stack.append((x,y))

def shoot(cnt, remain):
    global result, matrix
    if cnt == N:
        result = min(result, remain)
        return
    if remain == 0:
        result = 0
        return

    for j in range(W):
        for i in range(H):
            if matrix[i][j] != 0:
                if matrix[i][j] == 1:
                    matrix[i][j] = 0
                    next_remain = remain-1
                    shoot(cnt + 1, next_remain)
                    matrix[i][j] = 1
                else:
                    temp = [matrix[ii][:] for ii in range(H)]
                    dfs(i,j)
                    next_remain = gravity()
                    shoot(cnt+1, next_remain)
                    matrix = [temp[ii][:] for ii in range(H)]
                break


T = int(input())
for tc in range(1, 1+T):
    N, W, H = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(H)]
    result = float('inf')
    remain = 0
    for i in range(H):
        for j in range(W):
            if matrix[i][j] > 0:
                remain += 1
    shoot(0, remain)

    print(f'#{tc} {result}')