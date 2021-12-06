# numbers = {*""}
# numbers = {*{}}
# numbers = set()
# print(numbers, type(numbers))
#
# while len(numbers) < 4:
#     next_value = int(input("Enter the number: "))
#     numbers.add(next_value)
#
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]
# Creating a set from the list to avoid duplicating.
unique_data = sorted(set(data))
print(unique_data)


# Creating a list of unique colors chronologically.
unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data, 0))

