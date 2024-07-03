
import tkinter as tk
from math import factorial

def cal_factorial():
    
    num = int(entry.get())
    result = factorial(num)
    result_l.config(text=f"The factorial of {num} is: {result}")


window = tk.Tk()
window.title("get Factorial")
window.geometry("250x250")


label = tk.Label(window, text="Enter num:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Calculate", command=cal_factorial)
button.pack()

result_l = tk.Label(window, text="")
result_l.pack()

window.mainloop()