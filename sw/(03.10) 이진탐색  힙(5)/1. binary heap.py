import sys

sys.stdin = open('sample_input1.txt', 'r')

def change(i):
    if i == 1:
        return
    ch = arr[i]
    pa_i = i//2
    pa = arr[pa_i]
    if pa > ch:
        arr[i] = pa
        arr[pa_i] = ch
        change(pa_i)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0]
    arr.extend(list(map(int, input().split())))

    for i in range(N+1):
        change(i)



    nord = N
    result = 0
    while nord > 1:
        nord //= 2
        result += arr[nord]
    print(f'#{tc} {result}')
