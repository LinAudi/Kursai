print("STRING STARTING WITH VOWELS. \n")

def start_with_vowel(strings):
    return list(filter(lambda word: word[0].lower() in 'aeiou', strings))

print(start_with_vowel(["apple", "banana", "orange", "ice-cream"]))  # Output: ["apple", "orange"]