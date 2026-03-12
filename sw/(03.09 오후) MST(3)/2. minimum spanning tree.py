import sys

sys.stdin = open('sample_input2.txt', 'r')

def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]

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
    N, E = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    arr.sort(key=lambda x: x[2])
    parent = [i for i in range(N+1)]
    result = 0

    for i, ii, k in arr:
        connect = union(i,ii)
        if connect == True:
            result += k
        if sum(parent) == 0:
            break
    print(f'#{tc} {result}')