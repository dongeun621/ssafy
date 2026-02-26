import sys

sys.stdin = open('sample_input16.txt', 'r')

from itertools import permutations, product
from collections import deque
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    P_list = []
    S_list = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                P_list.append([i,j])
            elif matrix[i][j] > 1:
                S_list.append([i,j,matrix[i][j]])

    for i, p in enumerate(P_list):
        for s in S_list:
            t = abs(p[0]-s[0]) + abs(p[1]-s[1])
            P_list[i].append(t+1)
    n = len(P_list)
    arr = [2]*n
    arr.extend([3]*n)
    min_time = 9999
    for cellect in product([2,3], repeat=n):
        first_s = []
        second_s = []
        for i, j in enumerate(cellect):
            if j == 2:
                first_s.append(P_list[i][j])
            elif j == 3:
                second_s.append(P_list[i][j])
        first_s.sort(reverse=True)
        second_s.sort(reverse=True)

        t = 0
        first_q = deque()
        second_q = deque()
        while first_s or second_s or first_q or second_q:
            t += 1
            #계단내려가는 시간 +1
            for i in range(len(first_q)):
                first_q[i] += 1
            for i in range(len(second_q)):
                second_q[i] += 1
            #계단 내려가면 pop
            while first_q and first_q[0] == S_list[0][2]:
                first_q.popleft()
            while second_q and second_q[0] == S_list[1][2]:
                second_q.popleft()
            #계단도착한 사람들 자리비면 계단 들어가기
            while first_s and first_s[-1] <= t and len(first_q) < 3:
                first_s.pop()
                first_q.append(0)
            while second_s and second_s[-1] <= t and len(second_q) < 3:
                second_s.pop()
                second_q.append(0)
        min_time = min(min_time, t)
    print(f'#{tc} {min_time}')

