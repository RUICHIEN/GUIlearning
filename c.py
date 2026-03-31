import pandas as pd

class StockTracker:
    def __init__(self, prices):
        self.prices = pd.Series(prices)

    def moving_average(self, W):
        ma = self.prices.rolling(window=W).mean()
        ma = ma.fillna(0.0)
        return ma

# 輸入
N, W = map(int, input().split())
prices = list(map(int, input().split()))

# 建立物件
tracker = StockTracker(prices)

# 計算
result = tracker.moving_average(W)

# 輸出（保留1位小數）
print(" ".join(f"{x:.1f}" for x in result))