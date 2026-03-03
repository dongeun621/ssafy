import sys

sys.stdin = open('sample_input21.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    day, month, three, year = map(int, input().split())
    plan = list(map(int, input().split()))
    arr = [0]
    result = year
    for i in range(12):
        day_cost = plan[i]*day + arr[i]
        month_cost = month + arr[i]
        three_cost = three
        if i > 1:
            three_cost = three + arr[i-2]
        arr.append(min(day_cost, month_cost, three_cost))
    result = min(result, arr[-1])
    print(f'#{tc} {result}')