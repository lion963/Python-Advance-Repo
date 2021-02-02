def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def last(num1, num2):
    return num1 ** num2


mapper = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': division,
    '^': last
}


def math_operations(operator, num1, num2):
    result = mapper[operator](num1, num2)
    return result
