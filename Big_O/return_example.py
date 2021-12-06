def centered_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text))//2
    return ' ' * left_margin + text


with open("menu", mode='w') as menu:
    s1 = centered_text("an example")
    print(s1, file=menu)
    s2 = centered_text("a bigger example")
    print(s2, file=menu)
    print(centered_text(12), file=menu)
    print(centered_text("the biggest example"), file=menu)
    print(centered_text("first", "second", 3, 4, "fifth", sep='-'), file=menu)