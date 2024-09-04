def add(x: int, y: int) -> int:
    return x + y


def sub(x: int, y: int) -> int:
    return x - y


def prod(x: int, y: int) -> int:
    return x * y


def div(x: int, y: int) -> int:
    return x // y

x = 10
y = 2

add_answer = add(x, y)
sub_answer = sub(x, y)
prod_answer = prod(x, y)
div_answer = div(x, y)

print(add_answer)
print(sub_answer)
print(prod_answer)
print(div_answer)
