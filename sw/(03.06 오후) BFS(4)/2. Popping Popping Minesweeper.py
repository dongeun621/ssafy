import sys

sys.stdin = open('sample_input2.txt', 'r')

dxy = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    num_list = []
    result = 0
    # 주변에 지뢰가 있는 숫자칸은 전부 1로 표시
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.':
                for dx, dy in dxy:
                    x = i+dx
                    y = j+dy
                    if 0 <= x < N and 0 <= y < N and matrix[x][y] == '*':
                        matrix[i][j] = 1
                        break

    # 주변에 0이 없는 (.이 없는) 숫자는 따로 눌러줘야되므로 결과에 + 1
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                signal = 0
                for dx, dy in dxy:
                    x = i+dx
                    y = j+dy
                    if 0 <= x < N and 0 <= y < N and matrix[x][y] == '.':
                        signal = 1
                        break
                if signal == 0:
                    result += 1
    # 0인(.인) 덩어리 수 만큼 결과에 +1
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.':
                stack = [(i,j)]
                matrix[i][j] = 0
                while stack:
                    r, c = stack.pop()
                    for dx, dy in dxy:
                        x = r + dx
                        y = c + dy
                        if 0 <= x < N and 0 <= y < N and matrix[x][y] == '.':
                            matrix[x][y] = 0
                            stack.append((x,y))
                result += 1
    print(f'#{tc} {result}')
