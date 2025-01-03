class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def  __is_valid_color(self,a, b, c):
        return all(0 <= x <= 255 for x in (a, b, c))

    def set_color(self, a, b, c):
        if self.__is_valid_color(a, b, c):
            self.__color = [a, b, c]

    def __is_valid_sides(self, *n_sides):
        return len(n_sides) == self.sides_count and all(isinstance(x, int) and x > 0 for x in n_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *n_sides):
        if self.__is_valid_sides(*n_sides):
            self.__sides = list(n_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, length):
        super().__init__(color, length)
        self.__radius = length / (1 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        s = sum(self.get_sides()) / 2
        return (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge):
        sides = [edge] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        edge = self.get_sides()[0]
        return edge ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
