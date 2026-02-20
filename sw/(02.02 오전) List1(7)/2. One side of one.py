import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input()))
    dusthr = 0
    result = 0
    for i in num:
        if i == 1:
            dusthr += 1
            if dusthr > result:
                result = dusthr
        else:
            dusthr = 0
 
    print(f'#{test_case} {result}')