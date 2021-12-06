from operator import itemgetter


def search(sequence, expected, finder):
    for item in sequence:
        if finder(item) == expected:
            return item
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "HarryPotter", "age": 24},
    {"name": "Hermione", "age": 22},
    {"name": "RonWeasley", "age": 23}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Hermione", get_friend_name))
print(search(friends, "Hermione", lambda friend: friend["name"]))
print(search(friends, "Hermione", itemgetter("name")))