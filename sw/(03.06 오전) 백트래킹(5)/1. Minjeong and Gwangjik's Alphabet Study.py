import sys

sys.stdin = open('sample_input1.txt', 'r')

from itertools import product

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    words = []
    for _ in range(N):
        words.append(list(input().strip()))
    result = 0
    for words_list in product(range(2), repeat=N):
        alphabet = set()
        for i, flag in enumerate(words_list):
            if flag == 1:
                alphabet.update(words[i])
                if len(alphabet) == 26:
                    result += 1
                    break

    print(f'#{tc} {result}')