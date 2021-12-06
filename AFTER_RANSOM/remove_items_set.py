small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

small_ints.remove(10)
small_ints.discard(11)
print(small_ints)

small_ints.discard(99)
# small_ints.remove(99)  -> will give an error

print(small_ints)
print(sum(small_ints))