import pandas as pd

class Inventory:
    def __init__(self, items):
        # 建立 DataFrame
        self.df = pd.DataFrame(items, columns=["ItemName", "Price", "Quantity"])

    def calculate_total(self):
        # 新增一欄 Total_Value
        self.df["Total_Value"] = self.df["Price"] * self.df["Quantity"]

    def print_result(self):
        for _, row in self.df.iterrows():
            print(f"{row['ItemName']} {int(row['Total_Value'])}")


# === 主程式 ===
N = int(input().strip())

items = []
for _ in range(N):
    name, price, quantity = input().split()
    items.append([name, int(price), int(quantity)])

inv = Inventory(items)
inv.calculate_total()
inv.print_result()