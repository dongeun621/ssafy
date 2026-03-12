import sys

sys.stdin = open('sample_input5.txt', 'r')

for tc in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = {}
    result = [[S]]
    visited = [S]

    for i in range(0,N,2):
        if arr[i] in graph:
            graph[arr[i]].append(arr[i+1])
        else:
            graph[arr[i]] = [arr[i+1]]

    while True:
        stack = []
        for i in result[-1]:
            if i in graph:
                for j in graph[i]:
                    if j not in visited:
                        stack.append(j)
                        visited.append(j)
        if stack == []:
            break
        result.append(stack)

    print(f'#{tc} {max(result[-1])}')