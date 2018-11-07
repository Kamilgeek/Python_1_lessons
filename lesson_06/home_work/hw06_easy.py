import math
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Triangles:
    # функция-конструктор
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.AB = round(math.sqrt(int(bx - ax)**2 + (by - ay)**2))
        self.BC = round(math.sqrt(int(cx - bx)**2 + (cy - by)**2))
        self.AC = round(math.sqrt(int(ax - cx)**2 + (ay - cy)**2))

     #методы
    def perimeter(self):
        self.perimeter = self.AB + self.BC + self.AC
        return self.perimeter

    def area(self):
        self.perimeter /= 2
        self.area = round(math.sqrt(self.perimeter * (self.perimeter - self.AB)*(self.perimeter - self.BC)*(self.perimeter - self.AC)))
        return self.area

    def height(self):
        self.height = (2 * self.area) / self.AC
        return self.height


my_tri = Triangles(2, 2, 5, 8, 7, 4)
my_tri.perimeter()
print(my_tri.perimeter)
my_tri.area()
print(my_tri.area)
my_tri.height()
print(my_tri.height)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapeze:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy
        self.height = self.by - self.ay
        self.AB = round(math.sqrt(int(bx - ax) ** 2 + (by - ay) ** 2))
        self.BC = round(math.sqrt(int(cx - bx) ** 2 + (cy - by) ** 2))
        self.CD = round(math.sqrt(int(cx - dx) ** 2 + (cy - dy) ** 2))
        self.AD = round(math.sqrt(int(ax - dx) ** 2 + (ay - dy) ** 2))
    #ищем стороны
    def side_length(self):
        return self.AB, self.BC, self.CD, self.AD
    #проверяем является ли трапеция равнобочной
    def check(self):
        if self.AB == self.CD:
            print("Да, это равнобедренная трапеция.")
        else:
            print("Нет, это не равнобедренная трапеция.")
    #ищем периметр трапеции
    def perimeter_t(self):
        self.perimeter = self.AB + self.BC + self.AD + self.CD
        return self.perimeter
    #ищем площадь трапеции-
    def area_t(self):
        self.area = (self.AD + self.BC)/ 2 * self.height
        return self.area

my_trap = Trapeze(0, 0, 3, 5, 11, 5, 14, 0)
my_trap.side_length()
print(my_trap.side_length())
my_trap.perimeter_t()
print(my_trap.perimeter_t())
my_trap.check()
my_trap.area_t()
print(my_trap.area_t())

