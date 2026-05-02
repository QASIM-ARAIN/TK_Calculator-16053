import tkinter as tk
import math

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                label_result.config(text="Cannot divide by zero!", fg="red")
                return
            result = num1 / num2

        label_result.config(text=f"Result: {result}", fg="green")

    except ValueError:
        label_result.config(text="Invalid input! Enter numbers only.", fg="red")

def calculate_single(operation):
    try:
        num1 = float(entry_num1.get())

        if operation == "sq":
            result = num1 ** 2
        elif operation == "sqrt":
            if num1 < 0:
                label_result.config(text="Cannot find square root of negative!", fg="red")
                return
            result = math.sqrt(num1)

        label_result.config(text=f"Result: {result}", fg="green")

    except ValueError:
        label_result.config(text="Invalid input! Enter numbers only.", fg="red")


window = tk.Tk()
window.title("GUI Calculator")
window.geometry("350x350")
window.config(bg="#1e1e1e")


tk.Label(window, text="Enter First Number:", bg="#1e1e1e", fg="white").pack(pady=5)
entry_num1 = tk.Entry(window, width=30, justify="center")
entry_num1.pack()


tk.Label(window, text="Enter Second Number:", bg="#1e1e1e", fg="white").pack(pady=5)
entry_num2 = tk.Entry(window, width=30, justify="center")
entry_num2.pack()


frame1 = tk.Frame(window, bg="#1e1e1e")
frame1.pack(pady=10)

tk.Button(frame1, text="Add (+)", width=8, height=2, bg="#D17C69", fg="white",
          command=lambda: calculate("+")).pack(side="left", padx=5)
tk.Button(frame1, text="Sub (-)", width=8, height=2, bg="#D17C69", fg="white",
          command=lambda: calculate("-")).pack(side="left", padx=5)
tk.Button(frame1, text="Mul (*)", width=8, height=2, bg="#D17C69", fg="white",
          command=lambda: calculate("*")).pack(side="left", padx=5)
tk.Button(frame1, text="Div (/)", width=8, height=2, bg="#D17C69", fg="white",
          command=lambda: calculate("/")).pack(side="left", padx=5)


frame2 = tk.Frame(window, bg="#1e1e1e")
frame2.pack()

tk.Button(frame2, text="Square (x²)", width=12, height=2, bg="#3a86ff", fg="white",
          command=lambda: calculate_single("sq")).pack(side="left", padx=5)
tk.Button(frame2, text="Sqrt (√x)", width=12, height=2, bg="#3a86ff", fg="white",
          command=lambda: calculate_single("sqrt")).pack(side="left", padx=5)

label_result = tk.Label(window, text="Result: ", font=("Arial", 14), bg="#1e1e1e", fg="white")
label_result.pack(pady=10)

window.mainloop()
