import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str2_dict = {}
    result = 0
    for i in str2:
        if i in str2_dict:
            str2_dict[i] += 1
        else:
            str2_dict[i] = 1

    for i in range(len(str1)):
        if str1[i] in str2_dict:
            result = max(result, str2_dict[str1[i]])
    print(f"#{tc} {result}")