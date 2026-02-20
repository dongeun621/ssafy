import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [11, 7, 5, 3, 2]
    dit = {11:0, 7:0, 5:0, 3:0, 2:0}
 
    for i in arr:
        while N%i == 0:
            N /= i
            dit[i] += 1
 
    print(f'#{test_case} {dit[2]} {dit[3]} {dit[5]} {dit[7]} {dit[11]}')