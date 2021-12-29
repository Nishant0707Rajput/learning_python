

def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


def operation(*args, operator=None):
    if operator == "+":
        return sum(args)
    elif operator == "*":
        return multiply(*args)
    else:
        return "No valid operator provided"


print(operation(16,5,98,operator="+"))
print(operation(16,5,98,operator="*"))
print(operation(1,5,7))

