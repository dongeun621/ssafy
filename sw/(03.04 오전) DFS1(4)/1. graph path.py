import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]

    for _ in range(E):
        data = list(map(int, input().split()))
        arr[data[0]].append(data[1])

    S, G = map(int, input().split())
    visited = []
    stack = [S]
    while stack:
        i = stack.pop()
        if i in visited:
            continue
        visited.append(i)
        stack.extend(arr[i])
    result = 0
    if G in visited:
        result = 1

    print(f'#{tc} {result}')