import tkinter as tk

root = tk.Tk()
root.title("圈叉遊戲")

# 遊戲狀態變數
current_player = "X" # 追蹤目前是哪位玩家

# 用二維清單記錄棋盤（3 列 × 3 欄，初始全為空字串）
board = [["", "", ""],
 ["", "", ""],
 ["", "", ""]]

# 對應的按鈕物件也用二維清單儲存
buttons = [[None, None, None],
 [None, None, None],
 [None, None, None]]

# 狀態顯示標籤
label_status = tk.Label(root, text="玩家 X 的回合", font=("Arial", 13))
label_status.grid(row=3, column=0, columnspan=3, pady=8)

buttons = [[None]*3 for _ in range(3)]  # 儲存按鈕的二維清單

for row in range(3):
    for col in range(3):
        # 使用 lambda 捕捉當前的 row 和 col 值
        btn = tk.Button(
            root,
            text="",
            font=("Arial", 20, "bold"),
            width=4,
            height=2,
            command=lambda r=row, c=col: on_click(r, c)
        )
        btn.grid(row=row, column=col, padx=3, pady=3)
        # 儲存按鈕物件供後續操作
        buttons[row][col] = btn

def check_winner():
    # 檢查三橫行
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]
    # 檢查三縱列
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    # 檢查對角線
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    # 平局（所有格子都填滿）
    if all(board[r][c] != "" for r in range(3) for c in range(3)):
        return "平局"
    return None   # 遊戲繼續

def on_click(row, col):
    global current_player

    # 如果該格已有棋子，忽略點擊
    if board[row][col] != "":
        return

    # 更新資料（二維陣列）與畫面（按鈕文字）
    board[row][col] = current_player
    buttons[row][col].config(
        text=current_player,
        fg="blue" if current_player == "X" else "red"
    )

    # 切換玩家
    if current_player == "X":
        current_player = "O"
        label_status.config(text="玩家 O 的回合")
    else:
        current_player = "X"
        label_status.config(text="玩家 X 的回合")

    
def reset_game():
    global current_player, board, game_over

    current_player = "X"
    game_over = False

    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="")

    label_status.config(text="玩家 X 的回合")

btn_reset = tk.Button(root, text="重新開始", command=reset_game)
btn_reset.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()