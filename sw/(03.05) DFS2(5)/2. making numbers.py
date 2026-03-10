import sys

sys.stdin = open('sample_input2.txt', 'r')

def dfs(idx, score, stack):
    global max_score, min_score
    idx += 1
    if stack:
        for i in set(stack):
            next_score = score
            stack.remove(i)
            if i == 0:
                next_score += numbers[idx]
            elif i == 1:
                next_score -= numbers[idx]
            elif i == 2:
                next_score *= numbers[idx]
            elif i == 3:
                next_score //= numbers[idx]
                if score < 0 and score % numbers[idx] != 0:
                    next_score += 1

            dfs(idx, next_score, stack)
            stack.append(i)

    else:
        max_score = max(max_score, score)
        min_score = min(min_score, score)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    arr = []
    numbers = list(map(int, input().split()))
    max_score = -float('inf')
    min_score = float('inf')

    for i in range(4):
        dustkswk_list = [i]*A[i]
        arr.extend(dustkswk_list)

    dfs(0, numbers[0], arr)

    print(f'#{tc} {max_score-min_score}')