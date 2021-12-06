even = set(range(0, 100, 2))
squares = {1, 4, 9, 16, 25, 36, 49, 64, 100}
print("even minus square")
new_set = even.difference(squares)
print(new_set)
print(even - squares)
print("square minus even")
print(squares.difference(even))
print(squares - even)

even.difference_update(squares)
print(even)
