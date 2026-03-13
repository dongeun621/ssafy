import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    foods = [list(map(int, input().split())) for _ in range(N)]
    dp = [0]*(L+1)

    for s, c in foods:
        for i in range(L,c-1, -1):
            dp[i] = max(dp[i-c] + s, dp[i])
    print(f'#{tc} {dp[L]}')



