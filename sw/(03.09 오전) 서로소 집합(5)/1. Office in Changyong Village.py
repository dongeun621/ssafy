import sys

sys.stdin = open('sample_input1.txt', 'r')

def find(i):
    if parent[i] == i:
        return i
    return find(parent[i])

def union(a, b):
    A = find(a)
    B = find(b)
    if A == B:
        return
    elif A > B:
        parent[A] = B
    elif A < B:
        parent[B] = A

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    parent = [0]
    parent.extend([i for i in range(1, N+1)])
    result = 0
    for _ in range(M):
        i, j = map(int,input().split())
        union(i,j)

    for i, j in enumerate(parent):
        if i > 0 and i == j:
            result += 1
    print(f'#{tc} {result}')