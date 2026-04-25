import tkinter as tk
import random
user_score = 0
comp_score = 0
def play(user_choice):
    global user_score, comp_score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = f"You Win!\n{user_choice} beats {computer_choice}."
        user_score += 1
    else:
        result = f"Computer Wins!\n{computer_choice} beats {user_choice}."
        comp_score += 1
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")
root = tk.Tk()
root.title("Rock Paper Scissors Game") 
root.geometry("400x400")
instruction = tk.Label(root, text="Choose your move:", font=("Arial", 14), pady=10)
instruction.pack()
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue", pady=30)
result_label.pack()
root.mainloop()