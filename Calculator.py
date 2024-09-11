import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        # Creating display
        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Creating buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3, fg="purple")
        
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3, fg="blue")
        
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3, fg="black")
        
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2, command=self.calculate)
        self.create_button("+", 4, 3, fg="red")
        
        self.create_button("AC", 5, 0, columnspan=4, command=self.clear)

    def create_button(self, text, row, column, columnspan=1, command=None, fg="black"):
        if command is None:
            command = lambda: self.click(text)
        button = tk.Button(self.master, text=text, command=command, width=9, height=3, fg=fg)
        button.grid(row=row, column=column, columnspan=columnspan, padx=2, pady=2)

    def click(self, key):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, str(current) + str(key))

    def clear(self):
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()