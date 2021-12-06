from itertools import permutations
string = "BANANA"
Kevin = 0
Stuart = 0
# for i in range(1, len(string)+1):
#     for j in range(i):
#         # print(string[j:i])
#         if s
vowels = "AEIOU"
new_list = [string[i:j] for i in range(1, len(string)+1) for j in range(i)  ]
print(new_list)

# if Stuart > Kevin:
#     print(f"Stuart {Stuart}")
# elif Kevin > Stuart:
#     print(f"Kevin {Stuart}")
# else:
#     print("Draw")

