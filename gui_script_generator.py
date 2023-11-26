import tkinter as tk
from tkinter import scrolledtext

def generate_script():
    commands = command_text.get("1.0", tk.END).splitlines()
    script_name = script_name_entry.get()

    with open(script_name, 'w') as script_file:
        script_file.write('#!/bin/bash\n\n')
        for command in commands:
            script_file.write(command + '\n')

    result_label.config(text=f"Bash script '{script_name}' generated successfully!")

# GUI setup
root = tk.Tk()
root.title("Bash Script Generator")

# Command input area
command_text = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
command_text.pack(padx=10, pady=10)

# Script name input
script_name_label = tk.Label(root, text="Script Name:")
script_name_label.pack(padx=10, pady=(0, 5))
script_name_entry = tk.Entry(root)
script_name_entry.pack(padx=10, pady=(0, 10))

# Generate button
generate_button = tk.Button(root, text="Generate Script", command=generate_script)
generate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
