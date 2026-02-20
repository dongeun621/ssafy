import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case}')
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    cnt = 0
    for a, i in arr:
        for _ in range(int(i)):
            cnt += 1
            if cnt < 10:
                print(a, end='')
            else:
                cnt = 0
                print(a, end='\n')
    print('')