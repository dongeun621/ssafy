import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    corret = list(map(int, input().split()))
    max_score = 0
    min_score = 1000
 
    for _ in range(N):
        answer = list(map(int, input().split()))
        sum_score = 0
        score = 1
        for i in range(M):
            if answer[i] == corret[i]:
                sum_score += score
                score += 1
            else:
                score = 1
        max_score = max(max_score, sum_score)
        min_score = min(min_score, sum_score)
 
    print(f'#{tc} {max_score-min_score}')