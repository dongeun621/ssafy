import sys

sys.stdin = open('sample_input1.txt', 'r')

def pick(idx,size, price):
    if size > N:
        return

    for i in range(idx,M):
        if visited[i] == 0:
            pick(i+1,size+items[i][0], price+items[i][1])

    global max_price
    max_price = max(max_price, price)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(M)]
    max_price = 0
    visited = [0]*M

    pick(0,0,0)

    print(f'#{tc} {max_price}')

