import tkinter as tk
from tkinter import messagebox
def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())
        simple_interest = (p * t * r) / 100
        compound_interest = p * ((1 + r/100) ** t) - p
        result_label.config(
            text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#e6f2ff")
frame = tk.Frame(root, bg="#e6f2ff")
frame.pack(pady=20) 
tk.Label(frame, text="Principal:", bg="#e6f2ff").grid(row=0, column=0, padx=10, pady=10, sticky="e")
principal_entry = tk.Entry(frame)
principal_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Label(frame, text="Time (years):", bg="#e6f2ff").grid(row=1, column=0, padx=10, pady=10, sticky="e")
time_entry = tk.Entry(frame)
time_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Label(frame, text="Rate (%):", bg="#e6f2ff").grid(row=2, column=0, padx=10, pady=10, sticky="e")
rate_entry = tk.Entry(frame)
rate_entry.grid(row=2, column=1, padx=10, pady=10)
calc_button = tk.Button(root, text="Calculate", bg="#4da6ff", fg="white", command=calculate_interest)
calc_button.pack(pady=20)
result_label = tk.Label(root, text="", bg="#e6f2ff", font=("Arial", 12))
result_label.pack(pady=20)
root.mainloop()