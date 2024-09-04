print("REPEAT STRING. \n")

def repeat_string(string, number):
    r_string = string*int(number)
    return r_string

print(repeat_string("Hello", 3))

repeat_string = lambda string, number: string * number

print(repeat_string("LABAS", 5))