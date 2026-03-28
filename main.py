import csv
import os
from pathlib import Path
from product import Product
from receipt import Receipt
from database import Database


def prompt_str(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def prompt_int(prompt, min_value=None):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
            continue
        return value


def prompt_float(prompt, min_value=None):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value:.2f}.")
            continue
        return value


def ensure_sales_csv(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["product_name", "quantity", "total"])
            writer.writeheader()


def append_sales_csv(path: Path, products):
    ensure_sales_csv(path)
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["product_name", "quantity", "total"])
        for p in products:
            writer.writerow({"product_name": p.name, "quantity": p.quantity, "total": f"{p.get_total():.2f}"})


def run_pos():
    print("====== MiniPOS System ======")

    cashier = prompt_str("Enter cashier name: ")
    customer = prompt_str("Enter customer name: ")

    num_products = prompt_int("How many products? ", min_value=1)
    products = []

    for i in range(num_products):
        print(f"\nProduct {i + 1}")
        name = prompt_str("Product name: ")
        quantity = prompt_int("Quantity: ", min_value=0)
        price = prompt_float("Price: ", min_value=0.0)
        products.append(Product(name, quantity, price))

    receipt = Receipt(cashier, customer, products)
    receipt.print_receipt()

    total = receipt.get_grand_total()
    payment = prompt_float("Customer payment: ", min_value=total)

    change = payment - total
    print(f"Change: R{change:.2f}")

    csv_path = Path("data") / "sales.csv"
    append_sales_csv(csv_path, products)

    db = None
    try:
        db = Database()
        for p in products:
            db.insert_sale(p)
        print("Sales saved to MySQL and CSV")
    except Exception as exc:
        print(f"Warning: database operation failed ({exc}). CSV was saved.")
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    run_pos()
