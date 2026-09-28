import tkinter
import keyboard


window = tkinter.Tk()
window.title("PyKeys")
window.wm_attributes("-topmost", True)


def show_window():
    window.deiconify()


keyboard.add_hotkey("ctrl+alt+y", show_window)


def copy_symbol(symbol):
    window.clipboard_clear()
    window.clipboard_append(symbol)
    window.withdraw()


symbols = [
    "()", "[]", "{}", "''", '""', "'''", '"""',
    ":", ";", ",", ".", "_",
    "#", "@", "|", "\\",
    "=", "==", "!=", "+=", "-=",
    "+", "-", "*", "/", "//", "%",
    "**", "<", ">", "<=", ">=",
    "$", "€","!","&"
]


for row, symbol in enumerate(symbols):
    button = tkinter.Button(
        window,
        text=symbol,
        width=5,
        command=lambda s=symbol: copy_symbol(s)
    )
    button.grid(
        row=row // 5,
        column=row % 5,
        padx=3,
        pady=3
    )


window.mainloop()
