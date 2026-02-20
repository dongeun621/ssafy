import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    word = input()
    arr = [word[0]]
    cont_signal = 0
 
    for i in range(1, len(word)):
        if arr == []:
            arr.append(word[i])
        elif arr[-1] == word[i]:
            arr.pop()
        else:
            arr.append(word[i])
 
    print(f'#{test_case} {len(arr)}')