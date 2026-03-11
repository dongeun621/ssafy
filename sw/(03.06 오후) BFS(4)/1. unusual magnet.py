import sys

sys.stdin = open('sample_input1.txt', 'r')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    matrix = [deque(list(map(int, input().split()))) for _ in range(4)]
    k_list = [tuple(map(int, input().split())) for _ in range(K)]
    result = 0

    for k in range(K):
        m_idx, direct = k_list[k]
        m_idx -= 1
        dif = [0]*3
        #다른 자석들 체크
        for i in range(3):
            if matrix[i][2] != matrix[i+1][6]:
                dif[i] = 1
        matrix[m_idx].rotate(direct)
        #왼쪽으로 탐색
        next_direct = direct
        for i in range(m_idx-1,-1,-1):
            next_direct = -next_direct
            if dif[i] == 0:
                break
            matrix[i].rotate(next_direct)

        # 오른쪽으로 탐색
        next_direct = direct
        for i in range(m_idx+1,4):
            next_direct = -next_direct
            if dif[i-1] == 0:
                break
            matrix[i].rotate(next_direct)

    for i in range(4):
        if matrix[i][0] == 1:
            result += 2**i
    print(f'#{tc} {result}')

