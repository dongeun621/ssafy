import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = None
    for i in range(N):
        if result != None:
            break
        for j in range(0, N-M+1):
            word = arr[i][j:j+M]
            if word == word[::-1]:
                result = word

    for i in range(0, N-M+1):
        if result != None:
            break
        for j in range(N):
            word = ''.join(arr[ii][j] for ii in range(i,i+M))
            if word == word[::-1]:
                result = word

    print(f'#{tc} {result}')