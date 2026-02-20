import sys

sys.stdin = open('sample_input5.txt', 'r')

T = 10
for test_case in range(1, T+1):
    N = input()
    arr = list(input())
    stack1 = []
    stack2 = []
 
    for i in arr:
        if i.isdecimal():
            stack1.append(i)
        elif i == '+':
            if stack2:
                if stack2[-1] == '+':
                    stack1.append(i)
                elif stack2[-1] == '*':
                    stack1.append(stack2.pop())
                    stack2.append(i)
            else:
                stack2.append(i)
        elif i == '*':
            if stack2:
                if stack2[-1] == '+':
                    stack2.append(i)
                elif stack2[-1] == '*':
                    stack1.append(i)
            else:
                stack2.append(i)
    while stack2 != []:
        stack1.append(stack2.pop())
 
    for i in stack1:
        if i.isdecimal():
            stack2.append(int(i))
        elif i == '+':
            a = int(stack2.pop())
            b = int(stack2.pop())
            stack2.append(a+b)
        elif i == '*':
            a = int(stack2.pop())
            b = int(stack2.pop())
            stack2.append(a*b)
 
    print(f'#{test_case} {stack2[0]}')