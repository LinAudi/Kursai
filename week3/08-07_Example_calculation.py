print("Example calculation: \n")

def calculation(principal, rate, time):
    result = round(principal* (1+ rate) ** time,2)
    return result

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a decimal): "))
time = float(input("Enter the time in years: "))

print(f"The amount after {time} is {calculation(principal, rate, time)}.")