# def add(x, y):
#     return x-y
#
#
# a_dict = {"x": 3, "y": 8}
#
# print(add(**a_dict))    # ** to unpack named arguments
def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for key,val in kwargs.items():
        print(f"{key}: {val}")


# print_nicely(name= "Bob", age="22")

def args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


args_kwargs(1, 4, 6, name="Stuart", nick="Little")
