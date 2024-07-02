
import tkinter as tk

def reverse_word():
    original_word = entry.get()
    reversed_word = original_word[::-1]  
    result.config(text=f"Reversed word: {reversed_word}") 


root = tk.Tk()
root.title("mohamed khedr")

word = tk.Label(root, text="Enter a word: ")
word.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack()


reverse_button = tk.Button(root, text="validate", command=reverse_word)
reverse_button.pack(pady=10)


result = tk.Label(root, text="")
result.pack()


root.mainloop()

