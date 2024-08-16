import re
import tkinter as tk
from tkinter import messagebox

def assess_password_strength(password):
    length_weight = 2
    upper_weight = 1
    lower_weight = 1
    digit_weight = 1
    special_weight = 2

    score = 0

    length = len(password)
    if length >= 8:
        score += length_weight
        if length >= 12:
            score += length_weight  

    if re.search(r'[A-Z]', password):
        score += upper_weight

    if re.search(r'[a-z]', password):
        score += lower_weight

    if re.search(r'\d', password):
        score += digit_weight

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += special_weight

    if score >= 7:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    feedback = []
    if length < 8:
        feedback.append("Password is too short. Consider using at least 8 characters.")
    if not re.search(r'[A-Z]', password):
        feedback.append("Add uppercase letters to make your password stronger.")
    if not re.search(r'[a-z]', password):
        feedback.append("Add lowercase letters to make your password stronger.")
    if not re.search(r'\d', password):
        feedback.append("Include numbers to enhance your password security.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Include special characters to make your password more secure.")

    return {"strength": strength, "score": score, "feedback": feedback}

def check_password():
    password = entry.get()
    result = assess_password_strength(password)
    feedback_msg = "\n".join(result['feedback'])
    messagebox.showinfo("Password Strength", f"Strength: {result['strength']}\nScore: {result['score']}\nFeedback:\n{feedback_msg}")

def toggle_password():
    if show_password_var.get():
        entry.config(show='')
    else:
        entry.config(show='*')

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Create and place the widgets
tk.Label(root, text="Password Strength Checker", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=10)
tk.Label(root, text="Enter a password:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
entry = tk.Entry(root, show='*', font=("Helvetica", 12))
entry.pack(pady=5, padx=20)
show_password_var = tk.BooleanVar()
show_password_check = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password, bg="#f0f0f0", font=("Helvetica", 10))
show_password_check.pack()
tk.Button(root, text="Check Strength", command=check_password, font=("Helvetica", 12), bg="#4CAF50", fg="white", bd=0, relief="solid", highlightthickness=0, padx=10, pady=5).pack(pady=20)

# Start the GUI event loop
root.mainloop()