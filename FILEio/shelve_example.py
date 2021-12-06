import shelve

# with shelve.open("Shelftest") as fruit:
fruit = shelve.open("Shelftest")
# fruit["orange"] = "a sour, orange, citrus fruit"
# fruit["apple"] = "good for making cider"
# fruit["lemon"] = "a sour yellow citrus fruit"
# fruit["grape"] = "a small, sweet fruit growing in bunches"
# fruit["lime"] = "a sour green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ":" + fruit[snack])

# while True:
#     shelf_test = input("Please enter a fruit:")
#     if shelf_test.casefold() == "quit":
#         break
#     description = fruit.get(shelf_test, "We don't have " + shelf_test)
#     print(description)
for k in fruit.keys():
    print(k)
print(fruit.keys())

for v in fruit.values():
    print(v)
print(fruit.values())
for element in fruit.items():
    print(element)
print(fruit.items())

fruit.close()




