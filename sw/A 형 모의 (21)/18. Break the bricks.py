import sys

sys.stdin = open('sample_input18.txt', 'r')

def bricks(bmap, n):
    global result
    # 남은 횟수 0이면 벽돌개수 세서 비교
    if n == 0:
        cnt = 0
        for i in range(W):
            cnt += sum(matrix[i])
        result = max(result, cnt)

    for i in range(w):




T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    first_matrix = [list(map(int, input().split())) for _ in range(H)]
    matrix = [[] for _ in range(W)]
    result = 999

    for i in range(H-1, -1, -1):
        for j in range(W):
            matrix[j].append(first_matrix[i][j])

    bricks(matrix.copy(), N)