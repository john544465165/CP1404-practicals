def main():
    item = int(input("Enter the number of the item"))
    total_price = 0
    while item < 0:
        print("Invalid")
        item = int(input("Enter the number of the item"))
    for i in range(item):
        price = float(input("Enter the price of the item"))
        total_price = total_price + price
    if totle_price >= 100:
        total_price = total_price * 0.9
    print("The totle price for" + str(item) + "is" + str(total_price))
main()