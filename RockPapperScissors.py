import tkinter as tk
import random
def play_game(user_choice):
    choices = ['rock', 'paper', 'scissors']
    program_choice = random.choice(choices)
    user_var.set(user_choice.capitalize())
    program_var.set(program_choice.capitalize())
    if user_choice == program_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and program_choice == 'scissors') or \
         (user_choice == 'scissors' and program_choice == 'paper') or \
         (user_choice == 'paper' and program_choice == 'rock'):
        result = "You win!"
    else:
        result = "Program wins!"
    
    result_var.set(result)
def reset_game():
    user_var.set("")
    program_var.set("")
    result_var.set("")
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x300")
user_var = tk.StringVar()
program_var = tk.StringVar()
result_var = tk.StringVar()
tk.Label(window, text="Your Choice:").pack(pady=5)
tk.Label(window, textvariable=user_var, font=('Helvetica', 14)).pack(pady=5)
tk.Label(window, text="Program's Choice:").pack(pady=5)
tk.Label(window, textvariable=program_var, font=('Helvetica', 14)).pack(pady=5)
tk.Label(window, text="Result:").pack(pady=5)
tk.Label(window, textvariable=result_var, font=('Helvetica', 14)).pack(pady=5)
button_frame = tk.Frame(window)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Rock", command=lambda: play_game('rock')).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", command=lambda: play_game('paper')).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", command=lambda: play_game('scissors')).grid(row=0, column=2, padx=5)
tk.Button(window, text="Reset", command=reset_game).pack(pady=10)
window.mainloop()