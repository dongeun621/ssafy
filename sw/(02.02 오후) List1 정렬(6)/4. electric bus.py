import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    arr = [0]*(N+1) #충전소 위치
    a = 0   #버스 위치
    cnt = 0 #충전 횟수
    for i in M_list:
        arr[i] = 1
 
    while True:
        if a == N:
            break
        before_a = a
        for i in range(K,0,-1):
            if a+i > N: #1
                continue
            elif a+i == N: #2
                a = N
                break
            elif arr[a+i] == 1:
                a += i
                cnt += 1
                break
        if a == before_a: #3
            break
 
    if a < N:
        cnt = 0
    print(f'#{test_case} {cnt}')