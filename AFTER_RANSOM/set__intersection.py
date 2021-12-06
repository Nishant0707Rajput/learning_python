from primes_and_squares import primes_generator, squares_generator
evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(odds)
print(evens)


squares = set(squares_generator(100))
print(squares)

primes = set(primes_generator(100))
print(primes)

print(odds.intersection(squares))
print(evens & squares)

# pass an iterable to the method
even_squares = evens.intersection(squares_generator(100))
print(even_squares)