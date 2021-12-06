import shelve

blt = ["bacon", "lettuce", "tomato"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open("recipes", writeback=True) as recipes:
    recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    recipes["pasta"] = pasta

    # WILL not work in case of shelve
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

    # solution :-
    # temp_file = recipes["blt"]
    # temp_file.append("butter")
    # recipes["blt"] = temp_file

    # temp_file2 = recipes["pasta"]
    # temp_file2.append("tomato")
    # recipes["pasta"] = temp_file2

    recipes["blt"].append("this is added using writeback")
    # recipes["soup"] = soup



    for key in recipes:
        print(key, ":", recipes[key])

