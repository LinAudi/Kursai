def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed."
        return result

# Example Usage:
print(divide_numbers(10, 2))  # Outputs: 5.0
print(divide_numbers(10, 0))  # Outputs: Error: Division by zero is not allowed.
print(divide_numbers(10, 'a'))  # Outputs: Error: Both inputs must be numbers.