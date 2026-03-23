import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    one_len = len(str1)
    result = 0
    for i, a in enumerate(str2):
        if a == str1[0] and str2[i:i+one_len] == str1:
            result = 1
            break
    print(f'#{tc} {result}')
