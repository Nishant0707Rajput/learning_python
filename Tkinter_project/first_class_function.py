def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can't be zero")
    return dividend/divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(18, 3, operator=divide)
print(result)
