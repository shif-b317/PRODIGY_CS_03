import re
import tkinter as tk
from tkinter import messagebox

def check_password():
    password = entry.get()

    if not password.strip():
        messagebox.showwarning("Input Error", "Please enter password")
        return

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• At least 8 characters")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("• Add uppercase letters")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("• Add lowercase letters")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("• Include numbers")

    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        score += 1
    else:
        feedback.append("• Use special characters")

    if score <= 2:
        result_label.config(text="Weak ", fg="red")
    elif score <= 4:
        result_label.config(text="Moderate ", fg="orange")
    else:
        result_label.config(text="Strong ", fg="green")

    feedback_text.delete("1.0", tk.END)
    if feedback:
        feedback_text.insert(tk.END, "\n".join(feedback))
    else:
        feedback_text.insert(tk.END, " Strong password! No improvements needed.")


def exit_app():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.destroy()


root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x380")
root.resizable(False, False)

title = tk.Label(root, text=" Password Checker", font=("Arial", 16, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=10)

check_btn = tk.Button(root, text="Check Strength", command=check_password)
check_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=exit_app, bg="red", fg="white")
exit_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

feedback_text = tk.Text(root, height=6, width=40)
feedback_text.pack(pady=10)

root.mainloop()