import sys

sys.stdin = open('sample_input5.txt', 'r')

def order(i):
    if i == 0:
        return
    order(left[i])
    result.append(ch[i])
    order(right[i])

for tc in range(1, 11):
    N = int(input())
    ch = [0]
    left = [0] * (N+1)
    right = [0] * (N+1)
    result = []

    for _ in range(N):
        data = list(input().split())
        length = len(data)
        data[0] = int(data[0])
        ch.append(data[1])
        if length > 2:
            left[data[0]] = int(data[2])
        if length > 3:
            right[data[0]] = int(data[3])

    order(1)

    print(f'#{tc} {"".join(result)}')