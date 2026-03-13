import sys

sys.stdin = open('sample_input2.txt', 'r')

import math

T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    result = math.factorial(n) // (math.factorial(a) * math.factorial(b))
    print(f'#{tc} {result}')