import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    c_list = list(map(int, input().split()))
    cnt = 1
    max_cnt = 1
    for i in range(1, N):
        if c_list[i] > c_list[i-1]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
        if i == N-1:
            max_cnt = max(max_cnt, cnt)
 
    print(f'#{test_case} {max_cnt}')