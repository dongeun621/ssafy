import sys

sys.stdin = open('sample_input7.txt', 'r')

from collections import deque
T = int(input())
for tc in range(1, T+1):
    matrix = [deque(input()) for _ in range(5)]
    word = ''
    for i in range(15):
        for j in range(5):
            if matrix[j]:
                word += matrix[j].popleft()
 
    print(f'#{tc} {word}')