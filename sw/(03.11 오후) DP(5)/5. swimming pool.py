import sys

sys.stdin = open('sample_input5.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    day, month, three, year = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0]*12

    for i in range(12):
        if i < 3:
            dp[i] = min(dp[i-1]+arr[i]*day, dp[i-1]+month, three, year)
        else:
            dp[i] = min(dp[i-1]+arr[i]*day, dp[i-1]+month, dp[i-3]+three, year)
    print(f'#{tc} {dp[-1]}')
