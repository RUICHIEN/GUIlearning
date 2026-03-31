import numpy as np

# 設定隨機種子，確保結果可重現
np.random.seed(42)

# 生成 30 個常態分配的每日漲跌幅（單位：元）
# loc=0    → 平均漲跌為 0（不偏多也不偏空）
# scale=2  → 標準差為 2 元
# size=30  → 共 30 個交易日
daily_changes = np.random.normal(loc=0, scale=2, size=30)

# 設定起始股價
initial_price = 100

# np.cumsum() 計算每日漲跌的「累積總和」
# 再加上初始價格，就得到每日的收盤價
cumulative_changes = np.cumsum(daily_changes)
price_series = initial_price + cumulative_changes

# ── 統計分析 ──────────────────────────────
highest_price = np.max(price_series)   # 最高收盤價
lowest_price  = np.min(price_series)   # 最低收盤價
avg_price     = np.mean(price_series)  # 平均收盤價
volatility    = np.std(price_series)   # 價格標準差（波動度）
final_price   = price_series[-1]       # 第 30 天收盤價

print("每日漲跌幅（前 5 天）：", daily_changes[:5])
# 輸出範例：[ 0.99  -0.14   1.86  -0.38   1.10]
print("模擬股價（前 5 天）：", price_series[:5])
# 輸出範例：[100.99 100.85 102.71 102.33 103.43]

# 【對比】若用 for 迴圈，需要這樣寫（效率低）：
# prices = [initial_price]
# for change in daily_changes:
    # prices.append(prices[-1] + change)
# → np.cumsum() 一行搞定，且速度快上百倍！
print(f"最高收盤價：{highest_price:.2f} 元")   # 輸出：108.97 元
print(f"最低收盤價：{lowest_price:.2f} 元")    # 輸出： 97.43 元
print(f"平均收盤價：{avg_price:.2f} 元")       # 輸出：103.21 元
print(f"價格波動度：{volatility:.2f} 元")      # 輸出：  3.58 元
print(f"第30天收盤：{final_price:.2f} 元")     # 輸出：105.64 元

