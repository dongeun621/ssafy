import sys

sys.stdin = open('sample_input5.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
 
    t = D/(A+B)
    result = F*t
 
    print(f'#{tc} {result}')