import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    m = 0
    m_list = []
    dxy = [[1,0], [0,1], [-1,0], [0,-1]]
    result = 0
    for i in range(N):
        for j in range(N):
            m = max(m, matrix[i][j])
 
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == m:
                m_list.append([i,j])
 
    for i,j in m_list:
        cnt = 1
        break_signal = 0
        while True:
            low = 1000
            for ii, jj in dxy:
                if 0 <= i + ii < N and 0 <= j + jj < N:
                    low = min(low, matrix[i + ii][j + jj])
            for ii, jj in dxy:
                if 0 <= i + ii < N and 0 <= j + jj < N:
                    if matrix[i + ii][j + jj] == low:
                        if matrix[i][j] > low:
                            i = i + ii
                            j = j + jj
                            cnt += 1
                            break
                        else:
                            result = max(result, cnt)
                            break_signal = 1
                            break
            if break_signal == 1:
                break
    print(f'#{test_case} {result}')