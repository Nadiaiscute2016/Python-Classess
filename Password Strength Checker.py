import tkinter as tk
def check_strength():
    password = entry.get()
    length = len(password)
    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "light green"
    else:  # length > 12
        strength = "Very Strong"
        color = "dark green"
    result_label.config(text=strength, fg=color)
# Create main window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
# Widgets
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 14))
title_label.pack(pady=20)
entry = tk.Entry(root, show="*", width=25)
entry.pack(pady=10)
check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)
root.mainloop()