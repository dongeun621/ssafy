import sys

sys.stdin = open('sample_input5.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort(reverse=True)
    left = 0
    time = 0
    break_signal = 0
    result = 'Possible'
    while N > left:
        if people == []:
            break
        if time > 0 and time%M == 0:
            left += K
        while people[-1] == time:
            if left == 0:
                break_signal = 1
                break
            left -= 1
            people.pop()
            if people == []:
                break
        if break_signal == 1:
            result = 'Impossible'
            break
 
        time += 1
 
    print(f'#{test_case} {result}')