import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    m = 0
    dxy1 = [[1,0], [-1,0], [0,1], [0,-1]]
    dxy2 = [[1,1], [1,-1], [-1,1], [-1,-1]]
 
    for i in range(N):
        for j in range(N):
            s1 = matrix[i][j]
            s2 = matrix[i][j]
            for a,b in dxy1:
                for c in range(1, K):
                    if 0 <= i + a * c < N and 0 <= j + b * c < N:
                        s1 += matrix[i+a*c][j+b*c]
            for a,b in dxy2:
                for c in range(1, K):
                    if 0 <= i + a * c < N and 0 <= j + b * c < N:
                        s2 += matrix[i+a*c][j+b*c]
            m = max(m, s1, s2)
 
    print(f'#{test_case} {m}')