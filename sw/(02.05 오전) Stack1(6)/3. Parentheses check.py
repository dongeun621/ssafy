import sys

sys.stdin = open('sample_input3.txt', 'r')

dic = {
    ')' : '(',
    '}' : '{',
    ']' : '[',
}
 
T = int(input())
for test_case in range(1, T+1):
    a = list(input())
    result = 1
    b = []
    for i in a:
        if result == 0:
            break
        for j in dic.values():
            if i == j:
                b.append(i)
        for j in dic.keys():
            if i == j:
                if b == []:
                    result = 0
                    break
                elif dic[i] == b[-1]:
                    b.pop()
                else:
                    result = 0
                    break
    if b != []:
        result = 0
 
 
    print(f'#{test_case} {result}')