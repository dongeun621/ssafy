import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0]*8

    for i in range(8):
        cnt[i] = n//moneys[i]
        n %= moneys[i]

    print(f'#{tc}')
    print(*cnt)