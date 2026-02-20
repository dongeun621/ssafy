import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dic = {}
    dxy = [[1,0], [0,1], [-1,0], [0,-1]]
    # 메트릭스를 딕트로 바꿈
    for i in range(N):
        for j in range(M):
            if matrix[i][j] >= 1:
                #i 가 없으면 생성
                if i not in dic:
                    dic[i] = {}
                dic[i][j] = [matrix[i][j], 0]
 
    q = []
    for k in range(K):
        # dic에 세포 번식
        for info, i, j in q:
            # i가없으면 i추가
            if i not in dic:
                dic[i] = {}
            # 중복있으면 생명력수치가 높은 세포가 차지
            if j in dic[i]:
                dic[i][j][0] = max(dic[i][j][0], info[0])
            else:
                dic[i][j] = info
 
        # 분열할 세포 q에 추가
        q = []
        for i in dic:
            for j in dic[i]:
                dic[i][j][1] += 1 #사이클마다 시간 1 추가
                if dic[i][j][1] == dic[i][j][0]: #세포생성된 기간과 활성화 시간이 동일하면 다음사이클에 분열될 세포 q에 추가
                    for x,y in dxy: #델타탐색
                        if i+x not in dic:
                            q.append([[dic[i][j][1],-1], i+x, j+y])
                        else:
                            if j+y not in dic[i+x]:
                                q.append([[dic[i][j][1],-1], i+x, j+y])
 
 
    result = 0
    for i in dic:
        for j in dic[i]:
            if 2*dic[i][j][0] > dic[i][j][1]:
                result += 1
    print(f'#{tc} {result}')