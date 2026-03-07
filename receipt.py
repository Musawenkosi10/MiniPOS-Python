class Receipt:

    def __init__(self, cashier, customer, products):
        self.cashier = cashier
        self.customer = customer
        self.products = products

    def get_grand_total(self):

        total = 0

        for p in self.products:
            total += p.get_total()

        return total

    def print_receipt(self):

        print("\n====== RECEIPT ======")
        print("Cashier:", self.cashier)
        print("Customer:", self.customer)
        print("---------------------")

        for p in self.products:
            print(f"{p.name} x{p.quantity} = R{p.get_total():.2f}")

        print("---------------------")
        print(f"TOTAL: R{self.get_grand_total():.2f}")