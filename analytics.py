import pandas as pd
import matplotlib.pyplot as plt

def run_analytics():

    df = pd.read_csv("data/sales.csv")

    summary = df.groupby("product_name")["total"].sum()

    print("\nSales Summary:")
    print(summary)

    summary.plot(kind="bar")

    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")

    plt.savefig("charts/sales_chart.png")

    plt.show()