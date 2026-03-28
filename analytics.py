import pandas as pd
import matplotlib.pyplot as plt
import os

def run_analytics():

    df = pd.read_csv("data/sales.csv")

    summary = df.groupby("product_name")["total"].sum()

    print("\nSales Summary:")
    print(summary)

    summary.plot(kind="bar")

    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")

    os.makedirs("charts", exist_ok=True)
    plt.savefig("charts/sales_chart.png")

    plt.show()