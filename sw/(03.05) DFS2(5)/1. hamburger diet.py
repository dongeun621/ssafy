import sys

sys.stdin = open('sample_input1.txt', 'r')

def dfs(idx, score, cal):
    global max_score
    if cal > L:
        return
    else: max_score = max(max_score, score)

    for i in range(idx, food_cnt):
        dfs(i+1, score+foods[i][0], cal+foods[i][1])


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    foods = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    food_cnt = len(foods)

    dfs(0, 0, 0)

    print(f'#{tc} {max_score}')