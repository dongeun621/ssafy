import sys

sys.stdin = open('sample_input5.txt', 'r')

from heapq import heappop, heappush

def find(a):
    if parent[a] == a:
        return parent[a]
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    aa = find(a)
    bb = find(b)
    if aa == bb:
        return False
    if aa > bb:
        parent[aa] = bb
    elif bb > aa:
        parent[bb] = aa
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(2)]
    E = float(input())
    L = []
    parent = [i for i in range(N)]
    result = 0

    for i in range(N):
        for j in range(i+1, N):
            heappush(L, ((arr[0][i]-arr[0][j])**2+(arr[1][i]-arr[1][j])**2, i, j))

    for _ in range(len(L)):
        length, a, b = heappop(L)
        connect = union(a,b)
        if connect == True:
            result += length
        if sum(parent) == 0:
            break

    print(f'#{tc} {round(result*E)}')