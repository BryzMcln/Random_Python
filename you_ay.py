import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()
root.title("Button Example")

# Create a button
button = tk.Button(root, text="Click Me", command=button_clicked)
button.pack()

root.mainloop()
