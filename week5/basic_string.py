
def lower_upper(word1,word2):
    return word1.capitalize() + ", " + word2.upper()

def avg_word_length(word1,word2):
    first = len(word1)
    second = len(word2)
    return (first + second)/2

def longest_word(word1,word2):
    first = len(word1)
    second = len(word2)
    if first > second:
        return f"{word1.upper()} length is {first}"
    elif first < second:
        return f"{word2.upper()} length is {second}"
    else:
        return f"{word1} '= ' {word2}"

def did_u_win(x):
    import random

    num = random.randint(0,10)
    if x == num:
        return (f"U WON,LUCKY NUMBER: {num} ")
    else:
        return (f"U LOSE, lucky number was: {num}")
