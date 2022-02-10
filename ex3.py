class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def square(self):
        return f'Площадь = {self._length * self._width}'

    def perimeter(self):
        return f'Периметр = {2 * (self._length + self._width)}'

    @property
    def show_info(self):
        return f'Длина {self._length}, ширина {self._width}'

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    def set_width(self, a):
        if isinstance(a, (int, float)):
            self._width = a
        else:
            print('Введите правильное значение')

    def set_length(self, a):
        if isinstance(a, (int, float)):
            self._length = a
        else:
            print('Введите правильное значение')


r1 = Rectangle(5, 4)
print(r1.show_info)
r1.set_width(9)
r1.set_length(5)
print(r1.square())
print(r1.perimeter())
print(r1.show_info)