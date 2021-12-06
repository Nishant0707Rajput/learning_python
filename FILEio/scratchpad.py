# print("Adelaide".strip("idae"))
with open("sample.txt", 'r') as read_file:
    asdf = read_file.readline()
    while asdf:
        print(asdf.strip())
        asdf = read_file.readline()