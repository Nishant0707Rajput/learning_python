item_n = input()
quantity = int(input())
item = ["101", "102", "103", "104"]
item_name = ["Milk", "Cheese", "Ghee", "Bread"]
Price = [42, 50, 500, 40]
Stock = [10,20,15,16]
if item_n in item:
    val = item.index(item_n)
    if quantity<=Stock[val]:
        print(f"{quantity*Price[val]:.1f} INR")
        print(Stock[val]-quantity,"LEFT")
    elif quantity>Stock[val]:
        print("NO STOCK")
        print(Stock[val],"LEFT")
else:
    print("INVALID INPUT")

