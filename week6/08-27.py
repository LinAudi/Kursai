from random_word import RandomWords

r = RandomWords()

list = [r.get_random_word().upper() for _ in range (5)]

list_sorted = sorted(list)

for word in list_sorted:
    print(word)