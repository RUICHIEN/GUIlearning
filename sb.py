import pandas as pd
import numpy as np # 用 np.nan 表示缺失值

# 原始銷售資料（字典格式）
data = {
 '商品名稱': ['筆記型電腦', '無線滑鼠', '機械鍵盤', '顯示器', 'USB 集線器', '網路攝影機'],
 '類別': ['電腦', '周邊', '周邊', '電腦', '周邊', '周邊'],
 '單價': [35000, 650, 2800, 12000, 450, 1800],
 '銷售數量': [5, np.nan, 8, 3, np.nan, 6],
}

# 將字典轉換為 DataFrame
df = pd.DataFrame(data)
# 方法一：用 0 填補缺失值（假設缺失代表沒有銷售）
df['銷售數量'] = df['銷售數量'].fillna(0)

# 方法二（補充）：用平均值填補（更能反映一般銷售水準）
# df['銷售數量'] = df['銷售數量'].fillna(df['銷售數量'].mean())

# 新增「總金額」欄位 = 單價 × 銷售數量
# Pandas 會自動對每一列進行計算（向量化運算）
df['總金額'] = df['單價'] * df['銷售數量']

print("清理後的 DataFrame：")
print("\n是否還有缺失值：", df.isnull().any().any())  # 輸出：False
print(df)

# groupby('類別')：依「類別」欄位分組
# ['總金額']：選取要聚合的欄位
# .sum()：對每組進行加總
revenue_by_category = df.groupby('類別')['總金額'].sum()
print("各類別總營收：")
print(revenue_by_category)

# 進階：同時統計多個指標
summary = df.groupby('類別').agg(
    總營收=('總金額', 'sum'),
    商品數量=('商品名稱', 'count'),
    平均單價=('單價', 'mean')
)
print("\n進階統計摘要：")
print(summary)


