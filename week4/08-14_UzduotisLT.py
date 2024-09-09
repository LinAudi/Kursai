#1# Patys sukurkite bent 3 skirtingas funkcijas ir jas išbandykite
#
# def UPPERCASE_converter(fraze):
#     x = fraze.upper()
#     return x
#
# print(UPPERCASE_converter("labas storas"))
#
# def daugyba(x,y,z):
#     rezultatas = x * y * z
#     return rezultatas
#
# print(daugyba(5,8,9))

# def dalyba(x,y,z):
#     rezultatas = x / y / z
#     return rezultatas
#
# print(dalyba(360,2,5))
#
#
# #2# Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę.
#
# def pataisytas_list(*args):
#     x = [arg+"s" for arg in args]
#     return x
# print(pataisytas_list("medi","stora"))


#3# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.

#
#
# while True:
#
#
#     def skaiciuoklis(x,y):
#         suma = x+y
#         atimtis = x-y
#         dalyba = x/y
#         daugyba = x*y
#         return f"'Suma = '{suma}, 'Atimtis = '{atimtis}, 'Dalyba = '{dalyba}, 'Daugyba = '{daugyba}"
#
#     x = float(input("Enter number: "))
#     y = float(input("Enter Number: "))
#
#     print(skaiciuoklis(x,y))
#
#4# Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes.


# def unikalios_reiksmes(sarasas):

def unikalios_reiksmes(*args):

    naujas_sarasas = []
    for word in args:
        if len(set(word)) != len(word):
            naujas_sarasas.append(word)

    return naujas_sarasas

print(unikalios_reiksmes("Labas", "Medis", "Lopas", "Kaliošas"))



