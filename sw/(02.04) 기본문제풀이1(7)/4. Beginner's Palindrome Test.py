import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    word = input()
    result = 0
    if word == word[::-1]:
        result = 1
    print(f'#{test_case} {result}')