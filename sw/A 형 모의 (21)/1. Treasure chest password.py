import sys

sys.stdin = open('sample_input1.txt', 'r')

from collections import deque
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    num_list = deque(list(input()))
    sum_list = set()
    N = int(N/4)
    arr = [['A',10], ['B',11], ['C',12], ['D',13], ['E',14], ['F',15]]
    for i, j in enumerate(num_list):
        for a, b in arr:
            if j == a:
                num_list[i] = int(b)
            if '0' <= j <= '9':
                num_list[i] = int(j)
    for _ in range(N):
        for i in range(4):
            sum = 0
            for j in range(N):
                sum *= 16
                sum += num_list[j+N*i]
            sum_list.add(sum)
        num_list.rotate(1)
    sum_list = list(sum_list)
    sum_list.sort()
    print(f'#{test_case} {sum_list[-K]}')