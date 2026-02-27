import sys

sys.stdin = open('sample_input18.txt', 'r')

dxy = [[0,1], [1,0], [0,-1], [-1,0]]

def bricks(b_map, n):
    global result
    # 남은 횟수 0이면 벽돌개수 세서 비교
    if n == 0:
        cnt = 0
        for a in range(W):
            cnt += len(b_map[a])
        result = max(result, cnt)
        return

    for a in range(W):
        target = len(b_map[a])-1
        if not b_map[a]:
            continue
        if b_map[a][-1] != 1:
            new_map = dxy_search(b_map.copy(), a, target)
            new_map = [[x for x in row if x != 0] for row in new_map]
        else:
            new_map = [col[:] for col in b_map]
            new_map[a].pop()
        bricks(new_map, n-1)

def dxy_search(b_map_inner, x, y):
    K = b_map_inner[x][y]
    b_map_inner[x][y] = 0
    if K == 1:
        return b_map_inner
    for k in range(1, K):
        for dx, dy in dxy:
            xx = x + dx*k
            yy = y + dy*k
            if 0 <= x <W and len(b_map_inner[xx]) > y >= 0 and b_map_inner[xx][yy] != 0:
                b_map_inner = dxy_search(b_map_inner, xx, yy)

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    first_matrix = [list(map(int, input().split())) for _ in range(H)]
    matrix = [[] for _ in range(W)]
    result = 999

    for i in range(H-1, -1, -1):
        for j in range(W):
            if first_matrix[i][j] != 0:
                matrix[j].append(first_matrix[i][j])

    bricks(matrix.copy(), N)