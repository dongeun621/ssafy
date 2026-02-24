# 아래 클래스를 수정하시오.
class Dog:
    def __init__(self):
        self.sound = '멍멍'

class Cat:
    def __init__(self):
        self.sound = '야옹'


class Pet(Cat, Dog):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'
    
a = Pet()
print(a)
    


