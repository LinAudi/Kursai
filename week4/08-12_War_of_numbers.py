print("War of Numbers. \n")

def war_of_numbers(sarasas):
    even_sum =sum(x for x in sarasas if x % 2 ==0)
    odd_sum = sum(x for x in sarasas if x % 2 != 0)
    return abs(even_sum -odd_sum)
    # return even_sum -odd_sum


print(war_of_numbers([2,8,7,5]))
print(war_of_numbers([12, 90, 75]))
print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))