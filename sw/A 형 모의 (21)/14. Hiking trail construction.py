import sys

sys.stdin = open('sample_input8.txt', 'r')

dxy = [[1,0], [0,1], [-1,0], [0,-1]]
 
def search(high, i, j, viseted, cnt, Flag):
    global longest
    if Flag:
        #R : range 숫자
        R = 1+K
    else: R = 1
    viseted[i][j] = 1
    cnt += 1
 
    for ii, jj in dxy:
        if 0 <= i+ii < N and 0 <= j+jj < N and viseted[i+ii][j+jj] == 0:
            for r in range(R):
                next_hight = matrix[i+ii][j+jj]-r
                if high > next_hight:
                    if r > 0:
                        search(next_hight, i+ii, j+jj, viseted, cnt, False)
                    else:
                        search(next_hight, i+ii, j+jj, viseted, cnt, Flag)
                    break
    longest = max(longest, cnt)
    viseted[i][j] = 0
 
 
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    viseted = [[0]*N for _ in range(N)]
    #0 은 높이. 뒤에 최고봉 좌표들
    highest = [0]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > highest[0]:
                highest = [matrix[i][j], [i,j]]
            elif matrix[i][j] == highest[0]:
                highest.append([i,j])
    longest = 0
    for i,j in highest[1:]:
        search(highest[0], i, j, viseted, 0, True)
 
    print(f'#{tc} {longest}')