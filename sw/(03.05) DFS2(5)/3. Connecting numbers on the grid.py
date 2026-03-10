import sys

sys.stdin = open('sample_input3.txt', 'r')

dxy = [(-1,0), (0,1), (1,0), (0,-1)]

def dfs(i,j,idx, score):
    if idx == 7:
        result_set.add(score)
        return
    idx += 1
    for dx, dy in dxy:
        x = i + dx
        y = j + dy
        if 0 <= x < 4 and 0 <= y < 4:
            dfs(x,y,idx, score*10 + matrix[x][y])



T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(int,input().split())) for _ in range(4)]
    result_set = set()

    for i in range(4):
        for j in range(4):
            dfs(i,j,1,matrix[i][j])
    result = len(list(result_set))
    print(f'#{tc} {result}')