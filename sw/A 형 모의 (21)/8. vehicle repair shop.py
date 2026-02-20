import sys

sys.stdin = open('sample_input8.txt', 'r')

from collections import deque
 
T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    n_time = list(map(int, input().split()))
    m_time = list(map(int, input().split()))
    k_time = deque(map(int, input().split()))
    wait1 = deque()
    n_list = [[0, 0] for _ in range(N+1)] #[[고객번호, 접수, 정비], 시간]
    wait2 = deque()
    m_list = [[0, 0] for _ in range(M+1)] #[[고객번호, 접수, 정비], 시간]
    result = 0
    t = 0
    k = 1 #고객번호
    kk = 0 #정비끝난사람 숫자
    while kk < K:
 
        # 고객리스트에서 대기열1
        while k_time and k_time[0] == t:
            k_time.popleft()
            wait1.append([k, 0, 0])
            k += 1
        # 접수대에서 대기열2
        for i in range(1, N+1):
            if n_list[i][1] == n_time[i-1]:
                wait2.append(n_list[i][0])
                n_list[i] = [0, 0]
        # 대기열1에서 접수대
        for i in range(1, N+1):
            if wait1 and n_list[i][0] == 0:
                n_list[i][0] = wait1.popleft()
                n_list[i][0][1] = i
            if n_list[i][0] != 0:
                n_list[i][1] += 1
        # 정비대에서 아웃
        for i in range(1, M+1):
            if m_list[i][1] == m_time[i-1]:
                if m_list[i][0][1] == A and m_list[i][0][2] == B:
                    result += m_list[i][0][0]
 
                kk += 1
                m_list[i] = [0, 0]
        # 대기열2에서 정비대
        for i in range(1, M+1):
            if wait2 and m_list[i][0] == 0:
                m_list[i][0] = wait2.popleft()
                m_list[i][0][2] = i
            if m_list[i][0] != 0:
                m_list[i][1] += 1
        t += 1
    if result == 0:
        result = -1
    print(f'#{tc} {result}')