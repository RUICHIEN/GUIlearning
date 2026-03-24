import tkinter as tk
import random

choices = ["石頭", "剪刀", "布"]

def judge(player, computer):
    """判斷勝負，回傳結果字串"""
    if player == computer:
        return "平手！"
    elif (player == "石頭" and computer == "剪刀") or \
         (player == "剪刀" and computer == "布") or \
         (player == "布" and computer == "石頭"):
        return "你贏了！"
    else:
        return "電腦贏了！"

root = tk.Tk()
root.title("猜拳遊戲")
root.geometry("300x250")

label_prompt = tk.Label(root, text="請出拳！", font=("Arial", 14))
label_prompt.pack(pady=10)

# 建立一個 Frame 作為按鈕的容器
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

# 建立三個按鈕並綁定命令
for choice in choices:
    btn = tk.Button(
        btn_frame,
        text=choice,
        font=("Arial", 12),
        width=6,
        command=lambda c=choice: play(c)
    )
    # side=tk.LEFT 讓按鈕從左到右排列
    btn.pack(side=tk.LEFT, padx=8)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=5)

label_status = tk.Label(root, text="", font=("Arial", 13, "bold"), fg="blue")
label_status.pack(pady=10)


def play(player_choice):
    computer_choice = random.choice(choices)
    result = judge(player_choice, computer_choice)
    label_result.config(text=f"你出：{player_choice}  vs  電腦出：{computer_choice}")
    label_status.config(text=result)

root.mainloop()