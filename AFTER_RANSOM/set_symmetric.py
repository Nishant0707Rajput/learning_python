even = set(range(0, 50, 2))
squares = {0, 1, 4, 9, 16, 25, 36, 49,}
print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))