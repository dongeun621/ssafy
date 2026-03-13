import sys

sys.stdin = open('sample_input3.txt', 'r')



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dp = [0, 1, 3, 6]
    for i in range(4, N+1):
        dp.append(dp[i-1] + dp[i-2]*2 + dp[i-3])

    print(f'#{tc} {dp[-1]}')