# 아래 클래스를 수정하시오.
class StringRepeater:
    def __init__(self, n, word):
        self.number = n
        self.word = word

    def repeat_string(self):
        for _ in range(self.number):
            print(self.word)
    pass


repeater1 = StringRepeater(3, "Hello")
repeater1.repeat_string()
