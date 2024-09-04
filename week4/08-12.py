# name1 = "Jonas"
# name2 = "Petras"
# name3 = "Kazys"
# name4 = "Jurgis"
# #
# # *args - padaro tuple
# **kwargs - padaro zodyna

# def print_names(*args) :
#     # print(args)
#     for name in args:
#         print(name)
#
# def print_names(a,b,*args) :
#     # print(args)
#     for name in args:
#         print(f"a:{a}")
#         print(f"b:{b}")
#         print(f"args:{args}")
#
# print_names(name1,name2,name3)S
#

# def print_names(**kwargs):
#     print(kwargs)
#
#
# def suma(*args):
#     sum_result = sum(args)
#     return sum_result
#
# print(suma(1,2,5,6,7,8,9))
#
#
# def multiply(x,y):
#     return x*y
# print(multiply(20,10))
#
#
# lambda x,y: x*y
#
# print((lambda x,y: x*y)(3,5))


# new_numbers = []
# for number in numbers:
#     new_numbers.append(number/2)
# print(new_numbers)

#
# numbers = [-7, 5, 0, 10, -20, 3, 14, 1, 6]
#
# sorted_numbers = sorted(numbers, reverse = True, key=lambda x: x/2)
# sorted_numbers2 = sorted(numbers, key=lambda x: x/2)
#
# print(sorted_numbers)
# print(sorted_numbers2)

# numbers = [7, 4, 1, -2]
#
# sorted_numbers = sorted(numbers, key= lambda x: x % 2)
#
# print(sorted_numbers)

sakinys = ["as tu mes", "vienas du trys"]

sorted_sakinys = sorted(sakinys, key = lambda x: x.split()[1])
#['vienas du trys', 'as tu mes']
print(sorted_sakinys)