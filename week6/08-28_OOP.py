# #class - yra blueprint of house
#
# class House: #House gali but betkoks pavadinimas svarbu isdidziosio HouseHouseHouse
#     # pass # nieko nedaro tiesiog kaip kodas kad veiktu funkcija be kodo
#     def __init__(self):         # __inint__(konstruktorius) nekinta visada toks pavadinimas
#         self.cost = 200000
#         self.age = 15
#         self.doorcount = 1
#     def __str__(self): #leidzia grazinti stringa
#         return f"Cost: {self.cost}, age: {self.age}, Door count: {self.doorcount}"
#
# a = House() # du skirtingi namai
# b = House() # du skirtingi namai
#
#
#
# print(a.cost)
# print(a.age)
# print(a.doorcount)
# print(a)
#
# # a= {"cost": 20000,"age":15}
# #
# # print(a["cost"])              TAPATS KAS VIRSUI

class House:
    architect = "Jonas" # atributas bus pritaikytas betkuriam namui
    def __init__(self,cost,age,door_count):
        self.cost = cost
        self.age = age
        self.door_count = door_count
        self.print_cost()
    def print_cost(self):
        print(f'House build cost: {self.cost}')

    def __str__(self):
        return f"Cost: {self.cost},\n Age: {self.age},\n Door count: {self.door_count}\n"

a = House(20000,15,5)
b = House(150000,2,10)


print(a)
print(b)
print(House.architect)
print(a.architect)

House.architect = "Stasys"

print(a)
print(b)
print(House.architect)
print(a.architect)

class Expenses:
    def __init__(self):
        self.text = "tekstas"
        self.sum = "100"
        self.data = "2011-11-11"
