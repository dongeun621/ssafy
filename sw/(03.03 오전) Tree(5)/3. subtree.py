import sys

sys.stdin = open('sample_input3.txt', 'r')

def count(n):
    global result
    result += 1
    for child in arr[n]:
        count(child)

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    arr = [[] for _ in range(max(tree)+1)]
    result = 0
    for i in range(0,E*2,2):
        arr[tree[i]].append(tree[i+1])

    count(N)

    print(f'#{tc} {result}')