# 아래 함수를 수정하시오.
def count_character(a, b):
    cnt = 0
    for text in a:
        if text == b:
            cnt += 1        
    return cnt


result = count_character("Hello, World!", "o")
print(result)  # 2
