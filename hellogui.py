import tkinter as tk

# 建立主視窗（應用程式的根）
root = tk.Tk()

# 設定視窗標題
root.title("打招呼機器人")
# 設定視窗大小（寬 x 高）
root.geometry("300x200")
# 建立一個標籤，顯示提示文字
label_prompt = tk.Label(root, text="請輸入你的名字：", font=("Arial", 12))

# 定義打招呼函數（按下按鈕時執行）
def say_hello():
    name = entry_name.get()  # 讀取輸入框的文字
    label_result.config(text=f"哈囉，{name}！你好")

# 使用 pack() 將標籤放入視窗（由上而下排列）
label_prompt.pack()

# 建立輸入框，寬度為 20 個字元
entry_name = tk.Entry(root, width=20, font=("Arial", 12))
entry_name.pack()

btn = tk.Button(root, text="打招呼", command=say_hello)
btn.pack()

label_result = tk.Label(root, text="")
label_result.pack()

# 啟動事件迴圈（讓視窗持續運作）
root.mainloop()