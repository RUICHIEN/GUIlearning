import tkinter as tk
import random

root = tk.Tk()
root.title("圈叉遊戲：玩家 vs 電腦")

# 遊戲狀態
current_player = "X"   # 玩家固定是 X，電腦固定是 O
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

buttons = [[None] * 3 for _ in range(3)]


def check_winner():
    # 檢查橫列
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]

    # 檢查直行
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    # 檢查對角線
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    # 平局
    if all(board[r][c] != "" for r in range(3) for c in range(3)):
        return "平局"

    return None


def end_game(result):
    if result == "平局":
        label_status.config(text="平局！")
    else:
        label_status.config(text=f"玩家 {result} 獲勝！")

    for r in range(3):
        for c in range(3):
            buttons[r][c].config(state="disabled")


def get_empty_cells():
    empty_cells = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                empty_cells.append((r, c))
    return empty_cells


def find_best_move(symbol):
    """
    找出某個符號(symbol)是否有一步可以直接形成三連線
    有的話回傳那個位置，沒有就回傳 None
    """
    empty_cells = get_empty_cells()

    for r, c in empty_cells:
        board[r][c] = symbol
        if check_winner() == symbol:
            board[r][c] = ""
            return (r, c)
        board[r][c] = ""

    return None


def computer_move():
    global current_player

    # 1. 電腦自己能贏就先贏
    move = find_best_move("O")

    # 2. 否則擋玩家下一步可能的勝利
    if move is None:
        move = find_best_move("X")

    # 3. 搶中間
    if move is None and board[1][1] == "":
        move = (1, 1)

    # 4. 選角落
    if move is None:
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        available_corners = [pos for pos in corners if board[pos[0]][pos[1]] == ""]
        if available_corners:
            move = random.choice(available_corners)

    # 5. 選邊
    if move is None:
        sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
        available_sides = [pos for pos in sides if board[pos[0]][pos[1]] == ""]
        if available_sides:
            move = random.choice(available_sides)

    if move is not None:
        r, c = move
        board[r][c] = "O"
        buttons[r][c].config(text="O", fg="red")

        result = check_winner()
        if result:
            end_game(result)
            return

        current_player = "X"
        label_status.config(text="玩家 X 的回合")


def on_click(row, col):
    global current_player

    # 只允許玩家 X 點
    if current_player != "X":
        return

    # 如果該格已有棋子，忽略
    if board[row][col] != "":
        return

    # 玩家下棋
    board[row][col] = "X"
    buttons[row][col].config(text="X", fg="blue")

    result = check_winner()
    if result:
        end_game(result)
        return

    # 換電腦
    current_player = "O"
    label_status.config(text="電腦 O 思考中...")

    # 稍微延遲，讓畫面看起來自然一點
    root.after(300, computer_move)


def reset_game():
    global current_player, board

    current_player = "X"
    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", state="normal")

    label_status.config(text="玩家 X 的回合")


# 建立棋盤按鈕
for row in range(3):
    for col in range(3):
        btn = tk.Button(
            root,
            text="",
            font=("Arial", 20, "bold"),
            width=4,
            height=2,
            command=lambda r=row, c=col: on_click(r, c)
        )
        btn.grid(row=row, column=col, padx=3, pady=3)
        buttons[row][col] = btn

# 狀態顯示
label_status = tk.Label(root, text="玩家 X 的回合", font=("Arial", 13))
label_status.grid(row=3, column=0, columnspan=3, pady=8)

# 重新開始按鈕
btn_reset = tk.Button(root, text="重新開始", command=reset_game)
btn_reset.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()