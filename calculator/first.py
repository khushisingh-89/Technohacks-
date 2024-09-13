import tkinter as tk
from tkinter import messagebox


def click_button(value):
    current_text = entry.get()
    if value == "=":

        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
  
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            entry.delete(0, tk.END)
    elif value =="c":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)


root = tk.Tk()
root.title("Basic Calculator")


entry = tk.Entry(root, width=20, font=('Arial', 24), bd=10, insertwidth=4, borderwidth=4, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]


for i, button in enumerate(buttons):
    if button == "=":
        btn = tk.Button(root, text=button, width=5, height=2, command=lambda: click_button("="))
    else:
        btn = tk.Button(root, text=button, width=5, height=2, command=lambda b=button: click_button(b))
    row = i // 4+1
    col = i %4
    btn.grid(row=row, column=col, padx=5, pady=5)
    
clear_button = tk.Button(root, text="c", width=5, height=2, command=lambda: click_button("c"))
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)
  
root.mainloop()





    