import sys

sys.stdin = open('sample_input18.txt', 'r')

import copy
from collections import deque

dxy = [[0,1], [1,0], [0,-1], [-1,0]]

def shoot(copy_matrix, n):
    global result
    # 횟수가 없으면 0이 아닌 블록의 개수를 세서 결과 반영
    cnt = 0
    for i in range(H):
        for j in range(W):
            if copy_matrix[i][j] != 0:
                cnt += 1
    if n == 0 or cnt == 0:
        result = min(result, cnt)
        return

    # W만큼 구슬 발사
    for w in range(W):
        #w 별로 복사 메트릭스 제공
        second_copy_matrix = copy.deepcopy(copy_matrix)
        # 0이면 continue 아니면 타겟 지정
        target_h = None
        for h in range(H):
            if second_copy_matrix[h][w] == 0:
                continue
            else:
                target_h = h
                break
        # 0이 아닌 벽돌이 없으면 continue
        if target_h == None:
            continue

        # q로 탐색
        q = deque([[second_copy_matrix[target_h][w], target_h, w]]) #[k,h,w]
        while q: #deque가 빌 때까지
            target = q.popleft() # q에서 꺼내와서
            second_copy_matrix[target[1]][target[2]] = 0 # 해당좌표 0으로 만들고
            for k in range(1, target[0]): # k만큼 넓게 탐색
                for x, y in dxy: # dxy 탐색
                    x = x*k + target[1]
                    y = y*k + target[2]
                    if 0 <= x < H and 0 <= y < W and second_copy_matrix[x][y] > 0: # 0보다 크면 q에 넣기
                        q.append([second_copy_matrix[x][y], x, y])

        # 새 메트릭스에 중력적용된 메트릭스 씌움
        new_matrix = [[0]*W for _ in range(H)]
        for w in range(W):
            height = 1
            for h in range(H-1,-1,-1):
                if second_copy_matrix[h][w] > 0:
                    new_matrix[H-height][w] = second_copy_matrix[h][w]
                    height += 1

        shoot(new_matrix, n-1)



T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)] # matrix[H][W]
    result = 9999
    shoot(copy.deepcopy(matrix), N)
    print(f'#{tc} {result}')
