import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = N**2-1
 
    dxy = [[1,0], [-1,0], [0,1], [0,-1]]
 
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                monster = [i, j]
            elif matrix[i][j] == 1:
                result -= 1
 
    for a, b in dxy:
        for i in range(1, N):
            if 0 <= monster[0]+a*i < N and 0 <= monster[1]+b*i < N:
                if matrix[monster[0]+a*i][monster[1]+b*i] == 0:
                    result -=1
                else:
                    break
 
 
 
    print(f'#{test_case} {result}')