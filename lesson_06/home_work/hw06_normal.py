# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.
class Person:
    def __init__(self, name, surname, birth_day, school):
        self.name = name
        self.surname = surname
        self.birth_day = birth_day
        self.school = school
class Teacher(Person):
    def __init__(self, name, surname, birth_day, school, object, experience, class_rooms):
        Person.__init__(self, name, surname, birth_day, school)
        self.object = object
        self.experience = experience
class Student(Person):
    def __init__(self, name, surname, birth_day, school, class_room, objects):
        Person.__init__(self, name, surname, birth_day, school)
        self.class_room = class_room
        self.objects = objects
class Parent(Person):
    def  __init__(self, name, surname, birth_day, school,child):
        Person.__init__(self, name, surname, birth_day, school)
        self.child = child






# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

