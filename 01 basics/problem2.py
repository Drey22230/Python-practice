"""Problem 2
Create a program that asks for:

Product price
Quantity

Calculate the total.
"""
product_price = float(input("Enter the product price: "))
quantity = int(input("Enter the quantity: "))

total = product_price * quantity
print(f"The total is: ${total:.2f}")