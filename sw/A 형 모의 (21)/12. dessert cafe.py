import sys

sys.stdin = open('sample_input8.txt', 'r')

def search(ii, jj, current_direct):
    global result, i, j, direct
    desert_cnt.append(matrix[ii][jj]) #디저트 종류 추가
    visited[ii][jj] = 1 #방문기록 추가
    for next_direct in range(current_direct, current_direct+2):
        if next_direct - 5 == direct: #처음방향보다 한번 더 꺾으면 끝
            break
        iii = ii + dxy[next_direct][0] #다음 i
        jjj = jj + dxy[next_direct][1] #다음 j
 
        if iii == i and jjj == j: # 다음이 도착지면 끝
            result = max(result, len(desert_cnt))
            break
        elif 0 <= iii < N and 0 <= jjj < N and visited[iii][jjj] == 0 and matrix[iii][jjj] not in desert_cnt:
            search(iii, jjj, next_direct)  # 초기값 i,j 현재위치 ii,jj #디저트 수 #현재방향
    #방문기록, 디저트 종류 삭제
    desert_cnt.pop()
    visited[ii][jj] = 0
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    desert_cnt = []
    result = 0
    dxy = [[1,1], [1,-1], [-1,-1], [-1,1], [1,1], [1,-1], [-1,-1], [-1,1]]
 
 
    for i in range(N):
        for j in range(N):
            #초기에 방향 개수 카운트
            cnt = 0
            for x, y in dxy[:3]:
                ii = i+x
                jj = j+y
                if 0 <= ii < N and 0 <= jj < N and matrix[i][j] != matrix[ii][jj]:
                    cnt += 1
            if cnt <= 1: #방향 1개 이하면 탈락
                continue
 
            desert_cnt.append(matrix[i][j]) #디저트 종류 추가
            visited[i][j] = 1 #방문기록 추가
            for direct, xy in enumerate(dxy[:3]):
                ii = i + xy[0]
                jj = j + xy[1]
                if 0 <= ii < N and 0 <= jj < N and matrix[i][j] != matrix[ii][jj]:
                    search(ii, jj, direct) #현재위치 ii,jj #디저트 수 #현재방향
            desert_cnt.pop()  # 디저트 종류 추가
            visited[i][j] = 0
    if result == 0:
        result = -1
    print(f'#{tc} {result}')