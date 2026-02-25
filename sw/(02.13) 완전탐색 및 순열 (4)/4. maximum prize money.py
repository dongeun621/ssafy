import sys

sys.stdin = open('sample_input4.txt', 'r')

def dfs(arr, k):
    global result
    if k == K:
        s = 0
        for i in arr:
            s = s*10 + int(i)
        result = max(result, s)
        return
    for i in range(length-1):
        for j in range(i+1,length):
            a = arr[i]
            b = arr[j]
            arr[i] = b
            arr[j] = a
            visit = ''.join(arr)
            if visit not in visited[k]:
                visited[k].add(visit)
                dfs(arr,k+1)
            arr[i] = a
            arr[j] = b




T = int(input())
for tc in range(1, 1+T):
    N, K = input().split()
    K = int(K)
    N = list(N)
    visited = [set() for _ in range(K)]
    length = len(N)
    result = 0
    dfs(N, 0)
    print(f'#{tc} {result}')
