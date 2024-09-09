#1 Inheritance(Paveldejimas)

#Employee
class Employee:
    def __init__(self, name, age, experience, salary):
        self.name = name
        self.age = age
        self.experience = experience
        self.salary = salary

    def show(self):
        print(self.name, self.age, self.experience, self.salary)

#Engineers
class Engineer(Employee):
    def __init__(self,name, age, experience, salary, programing_language):
        super().__init__(name, age, experience, salary)          # tevines klases panaudojimui
        self.programing_language = programing_language
    def show(self):
        super().show()
        print(2+2)
    def say_hello(self):
        print("Hello")
#Designer

class Designer(Employee):
    def __init__(self, program):
        super().__init__()
        self.program = program

    def say_hello(self):
        print("Hello")

en = Engineer("Linas",30,5,2000,"Pyhon")
# des = Designer("Figma")

print(en.programing_language)
en.show()
en.age
print(en.name)
print(en.age)
print(en.experience)
print(en.salary)
#
# print(en.programing_language)
# print(des.name)
# print(des.age)
# print(des.experience)
# print(des.salary)

# #
# # # 2 Encapsulation
# # #




# # #
# # 3 Polymorphism
# #

# class Rectangule:
#     def __init__(self, l ,w):
#         self.l = l
#         self.w = w
#
#     def area(self):
#         return self.l * self.w
#
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return (self.radius ** 2)*3.14
#
# rectangle1 = Rectangule(10,20)
# square1 = Square(15)
# circle1 = Circle(10)
#
# shapes = [rectangle1, square1, circle1]
#
# for shape in shapes:
#     print(shape.area())
#
# # #
# # # 4 Abstraction
#
# def add(x,y, z=0):
#     return x+y+z
#
# print(add(1,2,3))
# print(add(1,2))