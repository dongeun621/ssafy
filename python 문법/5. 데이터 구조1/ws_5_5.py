# 아래 함수를 수정하시오.
def even_elements(list):
    result = []
    while list:
        num = list.pop(0)
        if num % 2 == 0:
            result.extend([num])

    return result


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
