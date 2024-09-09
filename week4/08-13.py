print("List comprehensions.\n")

# elements = [6,7,8,1]
#
# for x in range(len(elements)):
#     print(elements[x])
#
#
#
# squares = []
#
# for number in range(10):
#     squares.append(number*number)
# print(squares)
#
# squares = [number * number for number in range(11)]
# print(squares)
#
# squares = [number * number for number in range(11) if number != 5]
# print(squares)
#
# squares = [number * number for number in range(11) if number %2 == 0]
# print(squares)
#
#
# names = ["Albert", "Alma", "Joseph", "Zoro"]
#
# print([name for name in names if name.startswith("A")])
#
# squares = {name: name.upper() for name in names}
# print(squares)
#

#
# values = ["a", "b", "c"]
# index = 0
#
# for value in values:
#     print(index, value)
#     index += 1
# #
# values = ["a", "b", "c"]
# for count, value in enumerate(values):# enumerate istaukia indexa is saraso
#     print(count, value)
#
# values = ["a", "b", "c"]
# for count in enumerate(values):# enumerate istaukia indexa is saraso
#     print(count)
#
# values = ["a", "b", "c"]
# for count, value in enumerate(values, start= 100):# enumerate istaukia indexa is saraso
#     print(count, value)

#
# def even_items(numbers: list) -> list:
#     return [v for i, v in enumerate(numbers, start=1) if not i % 2]
#
# seq = list(range(1, 11))
#
# print(even_items(seq))
