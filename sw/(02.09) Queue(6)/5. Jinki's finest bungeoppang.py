import sys

sys.stdin = open('sample_input5.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    cos_list = list(map(int, input().split()))
    time = 0
    cnt = 0
    while N > cnt:
        if cos_list.count(0) > 0:
            break
        time += 1
        if time % M == 0:
            cnt += K
        a = cos_list.count(time)
        cnt -= a
        if cnt >= 0:
            N -= a
        else:
            break
 
    if N <= cnt:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')