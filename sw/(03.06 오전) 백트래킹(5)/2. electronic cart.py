import sys

sys.stdin = open('sample_input2.txt', 'r')

def backtrack(cnt, start, score):
    if len(visited) == N-1:
        global result
        result = min(result, score + matrix[start][0])
        return

    for i in range(1, N):
        if start == i or i in visited:
            continue
        d_score = matrix[start][i]
        visited.append(i)
        backtrack(cnt+1, i, score+d_score)
        visited.pop()
        matrix[start][i] = d_score



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    visited = []
    a = []
    result = float('inf')
    backtrack(0, 0, 0)

    print(f'#{tc} {result}')