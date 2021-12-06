val = int(input())
if 100 <= val <= 200:
    if val % 4 == 0:
        for i in range(4):
            print(val//4)
    elif val % 2 == 0:
        for i in range(4):
            print(val/4)
    else:
        for i in range(3):
            print(val//4)
        print(val//4+val%4)
else:
    print("INVALID INPUT")
