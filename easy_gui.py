import tkinter as tk
from tkinter import simpledialog

def write_bash_script():
    root = tk.Tk()
    root.withdraw()

    filename = simpledialog.askstring("Input", "Enter the name of the bash script:")
    command = simpledialog.askstring("Input", "Enter the command to be written in the bash script:")

    with open(filename, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write(command + "\n")

write_bash_script()
