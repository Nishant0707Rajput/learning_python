users = {
    (0, "Bob", "password"),
    (1, "Kevin", "New_password"),
    (2, "Stuart", "Rtuiopp"),
    (3, "rachel", "iwqpepj"),
    (4, "Nixon", "valure")
}

username_mapping = {user[1]: user for user in users}

# print(username_mapping)
# print(username_mapping["Bob"])  # --------> Top access user's data by name or something
# print(username_mapping["rachel"])

user_name = input("Input the user name:")
password_input = input("Input the password:")
_, name, password = username_mapping[user_name]
if password == password_input:
    print("You have logged in.")
else:
    print("Incorrect password")

