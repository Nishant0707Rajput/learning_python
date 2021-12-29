print((lambda x, y: x+y)(5,7))


a_lsit = [1, 2, 3, 4, 5]

doubled = [(lambda x:x*2)(x) for x in a_lsit]
print(doubled)

doubled = list(map(lambda x: x*2, a_lsit))
print(doubled)