# import  equations
import basic_string
#
# x = 10
# y = 2
#
# add_answer = equations.add(x, y)
# sub_answer = equations.sub(x, y)
# prod_answer = equations.prod(x, y)
# div_answer = equations.div(x, y)
#
# print(add_answer)
# print(sub_answer)
# print(prod_answer)
# print(div_answer)
#
#
# word1 = input("enter first word: ")
# word2 = input("enter second word: ")
#
# print(basic_string.lower_upper(word1, word2))
# print("average word length" ,basic_string.avg_word_length(word1, word2))
# print(basic_string.longest_word(word1, word2))
#
while True:
    name = input("Please enter your name: ")

    while True:
        x = int(input("please enter number(0-10): "))
        if 0 <= x <= 10:
            break
        else:
            print(f"wrong input.")

    print(basic_string.did_u_win(x))
