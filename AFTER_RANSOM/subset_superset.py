even = set(range(0, 50, 2))
squares = {0, 4, 16, 36}

if squares.issubset(even):
    print("squares is the subset of even.")

if even.issuperset(squares):
    print("even is the superset of squares.")


