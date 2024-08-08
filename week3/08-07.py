# def spausdinti_vardus():
#     vardai = ["Jonas", "Kazys", "Antanas"]
#
#     for vardas in vardai:
#         print(vardas) #Funkcija aprasyta
#     return 10
#
# print(spausdinti_vardus())
# spausdinti_vardus()#Funkcijai iskviesti
#
#
# def vardu_kiekis():
#     vardai = ["Jonas", "Kazys", "Antanas"]
#     ilgis = len(vardai)
#     return ilgis
#
# print(vardu_kiekis())

# def vardu_kiekis():
#     vardu_skaicius = 2
#     if vardu_skaicius > 3:
#         return "Daugiau"
#     else:
#         return "Maziau"
#
# vardu_skaicius = vardu_kiekis()
#
# print(vardu_skaicius)
# print(vardu_kiekis())

# def multiply_by_2():
#     number = 3
#     result = number * 2
#     return result
#
# print(multiply_by_2())

# def multiply_by_2(number):
#     result = number * 2
#     return result
#
# print(multiply_by_2(int(input("enter"))))
# print(multiply_by_2(10))

# def addition(number_one, number_two) :
#     result = number_one * 2
#     result2 = number_two * 2
#     return (result, result2)
# print(addition(5,10))
#

# def even_odd(num):
#     if num % 2 == 0:#iesko liekanos
#         return "Even"
#     else:
#         return "Odd"
# print(even_odd(11))

def addition(number_one = 0, number_two = 0):
    result = number_one + number_two
    return result
print(addition(10,0))
print(addition(0,20))
print(addition())

# print(round(1.18599,ndigits=3))
#
# print(round(251.18599,-1))

# numbers = [1,2,3,4,5,6,10,55,0,11,35]
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))