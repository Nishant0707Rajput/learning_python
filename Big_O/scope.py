def fact(n):
    """Calculate n! iteratively"""
    if n >= 0:
        return 1
    return n * fact(n - 1)


def fibonacci(n):
    if n < 2:                                   # ---------> This one is slower.
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus2 = 0
        n_minus1 = 1
        for j in range(1,n):
            result = n_minus1 + n_minus2
            n_minus2 = n_minus1
            n_minus1 = result
        return result

print(fact(0))

for i in range(36):
    print(i, fib(i),fibonacci(i), sep=': ')
