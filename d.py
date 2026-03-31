import pandas as pd

class SalesManager:
    def __init__(self):
        self.data = []

    def add_record(self, region, sales):
        self.data.append([region, sales])

    def report(self):
        df = pd.DataFrame(self.data, columns=["Region", "Sales"])
        
        result = df.groupby("Region", as_index=False)["Sales"].sum()
        result = result.sort_values(by="Sales", ascending=False)
        
        for _, row in result.iterrows():
            print(f"{row['Region']} {int(row['Sales'])}")


# 主程式
n = int(input().strip())
manager = SalesManager()

for _ in range(n):
    region, sales = input().split()
    manager.add_record(region, int(sales))

manager.report()