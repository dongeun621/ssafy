import sys
import time

sys.stdin = open('sample_input3.txt', 'r')

def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]
def union(a,b):
    A = find(a)
    B = find(b)
    if A == B:
        return
    elif A > B:
        parent[A] = B
    elif B > A:
        parent[B] = A
start_time = time.time()
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    parent = [0]
    parent.extend([i for i in range(1, N+1)])
    result = []

    for _ in range(M):
        k, a, b = map(int, input().split())
        if k == 0:
            union(a,b)
        elif k == 1:
            if find(a) == find(b):
                result.append('1')
            else:
                result.append('0')
    print(f"#{tc} {''.join(result)}")