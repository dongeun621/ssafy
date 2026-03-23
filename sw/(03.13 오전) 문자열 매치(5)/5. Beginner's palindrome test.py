import sys

sys.stdin = open('sample_input5.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    text = input()
    length = len(text)
    result = 0

    for i in range(length//2):
        if text[i] != text[-i-1]:
            break
        if i == length//2 - 1:
            result = 1

    print(f'#{tc} {result}')