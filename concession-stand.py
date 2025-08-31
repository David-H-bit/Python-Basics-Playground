import collections



menu = {
    "pizza": 3.00,
    "burger": 4.50,
    "fries": 2.00,
    "salad": 3.75,
    "soda": 1.50,
    "coffee": 2.25,
    "ice cream": 2.75,
    "sandwich": 3.25
}

cart = []
total = 0

print("-------------CONCESSION STAND-------------")
print()
print("-Order what you would like from the menu!-")

for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")

print()

while True:
    food = input("Enter an item (q to quit): ").lower()
    if food == "q":
        break
    elif food not in menu:
        print("please use valid items only!")
        print()
    elif food in menu:
        cart.append(food)
        total += menu.get(food)
        print(f"Added {food.title()}: (${menu[food]:.2f}), your current total is ${total:.2f}")


print("------------------------------------------")
print("Here is your order:")

order_summary = collections.Counter(cart)

for food, qty in order_summary.items():
    item_total = menu[food] * qty
    print(f"{food.title():10} x{qty:<10} ${item_total:.2f}")


print()
print(f"Your total is: ${total:.2f}")
