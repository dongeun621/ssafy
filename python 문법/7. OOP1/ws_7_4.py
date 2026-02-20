# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.a = w*h
        self.p = (w+h)*2

    def print_info(self):
        print(f'Width: {self.w}')
        print(f'Height: {self.h}')
        print(f'Area: {self.a}')
        print(f'Perimeter: {self.p}')


shape1 = Shape(5, 3)
shape1.print_info()
