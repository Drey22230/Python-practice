ProductName = input("Enter the product name: ")
ProductPrice = float(input("Enter the product price: "))
Quantity = int(input("Enter the quantity: "))
Cash = float(input("Enter the cash given: "))
TotalCost = ProductPrice * Quantity

Change = Cash - TotalCost if Cash >= TotalCost else 0

Inefficient = Cash < TotalCost 


needToPay = TotalCost - Cash if Inefficient else 0

print(f"Product Name: {ProductName}")
print(f"Product Price: ${ProductPrice:.2f}")
print(f"Quantity: {Quantity}")
print(f"Total Cost: ${TotalCost:.2f}")
print(f"Change: ${Change:.2f}")
if Inefficient:
    print("Insufficient cash provided. Please provide enough cash to cover the total cost.")
if Inefficient:
    print(f"You need to pay an additional: ${needToPay:.2f}")
