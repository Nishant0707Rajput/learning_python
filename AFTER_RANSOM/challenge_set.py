new_string: str = "A crazy brown fox jumped on the lazy dog."
vowels = frozenset("aeiou")
print(list(new_string))

# asf = list(new_string)
# char_set = set(asf)
# for j in asf:
#     if j.casefold() in vowels:
#         char_set.discard(j)
# print(sorted(char_set))


final_list = set(new_string).difference(vowels)
print(sorted(final_list))
