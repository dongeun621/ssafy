import sys

sys.stdin = open('sample_input2.txt', 'r')

from collections import deque
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    q = input()
    q = list(q)
    arr = [['A',10], ['B',11], ['C',12], ['D',13], ['E',14], ['F',15]]
    for i, a in enumerate(q):
        for b, c in arr:
            if a == b:
                q[i] = c
    q = deque(q)
    sum_list = []
    cnt = int(N/4)
    for _ in range(cnt):
        q.rotate(1)
        for i in range(4):
            sum = 0
            for j in range(cnt):
                idx = int(j+i*cnt)
                sum += int(q[idx]) * 16**(cnt-j-1)
            if sum_list.count(sum) == 0:
                sum_list.append(sum)
 
    sum_list.sort()
 
    print(f'#{test_case} {sum_list[-K]}')