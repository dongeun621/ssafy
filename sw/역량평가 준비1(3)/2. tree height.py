import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    goal = max(trees)
    tall_need = []
    one_c = 0
    two_c = 0
    result = 0
    for i in trees:
        if i < goal:
            tall_need.append(goal-i)
 
    for i in tall_need:
        one_c += i % 2
        two_c += i//2
 
    if one_c > two_c:
        result += one_c*2 - 1
    elif one_c == two_c:
        result += one_c*2
    elif one_c < two_c:
        result += one_c*2 + ((two_c-one_c)//3)*4
        if (two_c-one_c)%3 > 0:
            result += (two_c-one_c)%3 + 1
 
 
 
 
    print(f'#{test_case} {result}')