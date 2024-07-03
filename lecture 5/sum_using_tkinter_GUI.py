import tkinter as tk


def calculate_sum():
    num1 = int(num1_var.get())  
    num2 = int(num2_var.get())  
    result = num1 + num2
    result_var.set(f"Sum: {result}")  
    


root = tk.Tk()
root.title("Sum of Two Integers")
root.geometry("250x250+150+150")

num1_var = tk.StringVar()
num2_var = tk.StringVar()
result_var = tk.StringVar()


label_num1 = tk.Label(root, text="Enter first integer:")
label_num1.pack(pady=10)
entry_num1 = tk.Entry(root, textvariable=num1_var, width=20)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second integer:")
label_num2.pack(pady=10)
entry_num2 = tk.Entry(root, textvariable=num2_var, width=20)
entry_num2.pack()


calculate_button = tk.Button(root, text="Calculate Sum", command=calculate_sum)
calculate_button.pack(pady=10)


result_label = tk.Label(root, textvariable=result_var)
result_label.pack()


root.mainloop()
