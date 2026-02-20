import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    word = input()
    result = ''
 
    for i in range(len(word)-1, -1, -1):
        if word[i] == 'b':
            result += 'd'
        elif word[i] == 'd':
            result += 'b'
        elif word[i] == 'q':
            result += 'p'
        elif word[i] == 'p':
            result += 'q'
 
    print(f'#{test_case} {result}')