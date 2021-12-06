with open("tables.txt", 'a') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print(f"{i} times {j} is {i * j}", file=tables)
        print("-"*40, file=tables)


# practicing ........


# fruit = {"orange": "a sour, orange, citrus fruit", "apple": "good for making cider",
#          "lemon": "a sour yellow citrus fruit", "grape": "a small, sweet fruit growing in bunches",
#          "lime": "a sour green citrus fruit"}
# # ert = fruit.keys()
# # print(ert)
# # qwd = list(ert)
# # print(qwd)
# # wsd = list(fruit.values())
# inverse_fruit = {}
# for i, j in fruit.items():
#     inverse_fruit[j] = i
# print(inverse_fruit)
