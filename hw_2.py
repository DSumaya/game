class  Figure:
    unit = 'cm'
    def calculate_area(self):
        raise NotImplemented

    def info(self):
        raise NotImplemented

class Square(Figure):
    def __init__(self,side_length):
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        square_area = self.calculate_area()
        print(f'Square side length: {self.__side_length} {self.unit}, Area: {square_area} {self.unit}')


class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        rectangle_area = self.calculate_area()
        print(f'Rectangle length: {self.__length} {self.unit}, Rectangle width: {self.__width} {self.unit} '
              f'Area: {rectangle_area} {self.unit}')


figure_list =[Square(8), Square(4),
              Rectangle(4, 5), Rectangle(3,9), Rectangle(6,2)]
for figure in figure_list:
    figure.info()




