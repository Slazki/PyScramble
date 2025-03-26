import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import random

def run_obfuscator(input_path, output_path, encrypt_strings, inject_dummy):
    command = ["python", "obfuscator.py", "--input", input_path, "--output", output_path]
    if encrypt_strings:
        command.append("--encrypt-strings")
    if inject_dummy:
        command.append("--inject-dummy")

    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", f"Obfuscated file saved to:\n{output_path}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to obfuscate file:\n{e}")

def browse_input():
    filename = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if filename:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, filename)

def browse_output():
    filename = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
    if filename:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, filename)

def obfuscate():
    input_path = input_entry.get()
    output_path = output_entry.get()
    encrypt = encrypt_var.get()
    dummy = dummy_var.get()
    if not os.path.isfile(input_path):
        messagebox.showerror("Error", "Invalid input file.")
        return
    if not output_path:
        messagebox.showerror("Error", "Output path is required.")
        return
    run_obfuscator(input_path, output_path, encrypt, dummy)

# GUI setup
root = tk.Tk()
root.title("PyScramble GUI")
root.geometry("500x300")

# Input file
input_label = tk.Label(root, text="Input File:")
input_label.pack(pady=(10, 0))
input_frame = tk.Frame(root)
input_frame.pack()
input_entry = tk.Entry(input_frame, width=50)
input_entry.pack(side=tk.LEFT, padx=(0, 5))
browse_input_btn = tk.Button(input_frame, text="Browse", command=browse_input)
browse_input_btn.pack(side=tk.LEFT)

# Output file
output_label = tk.Label(root, text="Output File:")
output_label.pack(pady=(10, 0))
output_frame = tk.Frame(root)
output_frame.pack()
output_entry = tk.Entry(output_frame, width=50)
output_entry.pack(side=tk.LEFT, padx=(0, 5))
browse_output_btn = tk.Button(output_frame, text="Browse", command=browse_output)
browse_output_btn.pack(side=tk.LEFT)

# Encrypt strings option
encrypt_var = tk.BooleanVar()
encrypt_check = tk.Checkbutton(root, text="Encrypt String Literals", variable=encrypt_var)
encrypt_check.pack(pady=5)

# Dummy code injection option
dummy_var = tk.BooleanVar()
dummy_check = tk.Checkbutton(root, text="Inject Dummy Code (Anti-analysis)", variable=dummy_var)
dummy_check.pack(pady=5)

# Obfuscate button
obfuscate_btn = tk.Button(root, text="Obfuscate", command=obfuscate)
obfuscate_btn.pack(pady=10)

root.mainloop()
