import sys

sys.stdin = open('sample_input8.txt', 'r')

def research(i,j, not_direct):
    global time, visited
    # time, visited 처리
    time += 1
    visited[i][j] = 1
    # time 이 경과시간과 같으면 끝
    if time == L:
        return
 
 
    # i가 방향, 방향별 탐색, 지나온 방향 제외
    for direct in pipe[matrix[i][j]]:
        if not_direct == None or direct != not_direct:
            ii = i + dxy[direct][0]
            jj = j + dxy[direct][1]
            # 해당 방향에 리버스 방향이 있는지 확인
            if 0<=ii<N:
                if 0<=jj<M:
                    if pipe[matrix[ii][jj]] != 0:
                        if rev_dxy[direct] in pipe[matrix[ii][jj]]:
                            research(ii,jj,rev_dxy[direct])
                            # research호출 후 time -1
                            time -= 1
 
 
T = int(input())
for tc in range(1, T+1):
    # 맵 세로, 가로, 맨홀 세로, 가로, 탈출 경과 시간
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dxy = [[-1,0], [1,0], [0,-1], [0,1]]
    rev_dxy = [1,0,3,2]
    pipe = [0, [0,1,2,3], [0,1], [2,3], [0,3], [1,3], [1,2], [0,2]]
    time = 0
    visited = [[0]*M for _ in range(N)]
 
    research(R,C, None)
    result = sum(sum(visited[i]) for i in range(N))
 
    print(f'#{tc} {result}')