# # 1.
# class Calculator:
#
#     def add(self, x, y):
#         return x + y
#
#     def subtract(self, x, y):
#         return x - y
#
#     def multiply(self, x, y):
#         return x * y
#
#     def divide(self, x, y):
#         try:
#             return x / y
#         except ZeroDivisionError:
#             return "Cannot divide by zero!"
#
# calc = Calculator()
# print(calc.add(10, 0))  # 8
# print(calc.subtract(10, 0))  # 6
# print(calc.multiply(10, 0))  # 42
# print(calc.divide(10, 0))  # 5.0

# # 2
#
# class Employee:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.fullname = f"{name}, {surname}"
#         self.email = f"{name.lower()}.{surname.lower()}@company.com"
#
#     def print_name(self):
#         print(self.fullname)
#         print(self.email)
#
# # name = input("Enter your name:").capitalize()
# # surname = input("Enter your surname:").capitalize()
#
# emp0001 = Employee("Linas","Surname")
# emp0001.print_name()
# emp0002= Employee("Storas","Medis")
# emp0001.print_name()

#3

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def get_title(self):
#         print(f"Book title: {self.title}")
#     def get_author(self):
#         print(f"Book Author: {self.author}")
#     def get_price(self):
#         print(f"Book price: {self.price} Eu")
#
#
# book1 = Book("Medžių šaknys","Aukštas medis",30)
#
# book1.get_title()
# book1.get_author()
# book1.get_price()
#

# 4

class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.population > 20_000_000 or self.area > 3_000_000

    def population_density(self):
        return self.population / self.area

    def compare_pd(self, other_country):
        if self.population_density() > other_country.population_density():
            return f"{self.name} has a larger density than {other_country.name}"
        else:
            return f"{other_country.name} has a larger density than {self.name}"


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
lithuania = Country("Lithuania", 2_880_000, 65300)
latvia = Country("Latvia", 1_900_000, 64589)

print(lithuania.compare_pd(latvia))
print(latvia.compare_pd(lithuania))

print(australia.population_density())
print(lithuania.population_density())
print(latvia.population_density())

print(australia.is_big)
print(andorra.is_big)
print(lithuania.is_big)