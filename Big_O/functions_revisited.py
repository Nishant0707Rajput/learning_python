def centered_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text))//2
    print(' ' * left_margin, text, end=end, file=file, flush=flush)


centered_text("an example")
centered_text("a bigger example")
centered_text(12)
centered_text("the biggest example")

centered_text("first", "second", 3, 4, "fifth", sep='-')