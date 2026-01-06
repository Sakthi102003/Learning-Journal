item = input("Enter the item you need to buy: ")
price = float(input("Enter the price?: "))
quantity = int(input("Enter the quantity of : "))

total = price * quantity
print(f"The total cost for {quantity} {item}(s) is: ${total}")