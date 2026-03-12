import sys

sys.stdin = open('sample_input3.txt', 'r')

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    A = find(a)
    B = find(b)
    if A == B:
        return False
    elif A > B:
        parent[A] = B
    elif B > A:
        parent[B] = A
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    island = [list(map(int, input().split())) for _ in range(2)]
    K = float(input())
    graph = []
    parent = [i for i in range(N)]
    result = 0

    for i in range(N):
        for j in range(i+1,N):
            i_x = island[0][i]
            i_y = island[1][i]
            j_x = island[0][j]
            j_y = island[1][j]
            distant = round((i_x-j_x)**2 + (i_y-j_y)**2, 1)
            graph.append([distant,i,j])

    graph.sort()

    for d, i, j in graph:
        connect = union(i,j)
        if connect == True:
            result += d

    print(f'#{tc} {int(round(result*K, 0))}')
