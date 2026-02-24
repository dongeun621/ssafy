# 아래 함수를 수정하시오.
def find_min_max(list):
    init1 = 0
    init2 = 0
    for a in list:
        if init1 == 0:
            init1 = 1
            min = a
        elif min > a:
            min = a
    for a in list:
        if init2 == 0:
            init2 = 1
            max = a
        elif max < a:
            max = a
    return (min, max)


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
