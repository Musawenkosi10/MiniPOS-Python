from product import Product
from receipt import Receipt
from database import Database
import csv

print("====== MiniPOS System ======")

cashier = input("Enter cashier name: ")
customer = input("Enter customer name: ")

num_products = int(input("How many products? "))

products = []

for i in range(num_products):

    print("\nProduct", i + 1)

    name = input("Product name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    product = Product(name, quantity, price)

    products.append(product)

receipt = Receipt(cashier, customer, products)

receipt.print_receipt()

total = receipt.get_grand_total()

payment = float(input("Customer payment: "))

change = payment - total

print("Change:", change)

db = Database()

with open("data/sales.csv", "a", newline="") as file:

    writer = csv.writer(file)

    for p in products:

        writer.writerow([
            p.name,
            p.quantity,
            p.get_total()
        ])

        db.insert_sale(p)

print("Sales saved!")