import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def calculate_death():
    try:
        dob = datetime.strptime(entry.get(), "%Y-%m-%d")
        gender = gender_var.get()

        if gender == "Male":
            life_expectancy = 73
        elif gender == "Female":
            life_expectancy = 78
        else:
            life_expectancy = 75

        death_date = dob.replace(year=dob.year + life_expectancy)
        now = datetime.now()

        if now > death_date:
            result = "💀 You are living on bonus time, my friend..."
        else:
            time_left = death_date - now
            days_left = time_left.days
            years = days_left // 365
            months = (days_left % 365) // 30
            days = (days_left % 365) % 30

            result = f"☠️ Estimated Death Date: {death_date.date()}\n🕰️ Remaining: {years} years, {months} months, {days} days"

        output.config(text=result)

    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter DOB in YYYY-MM-DD format.")

root = tk.Tk()
root.title("☠️ Death Clock - Hell Mode")
root.geometry("450x350")
root.configure(bg="black")

tk.Label(root, text="Enter your Date of Birth (YYYY-MM-DD):", font=("Helvetica", 12),
         fg="white", bg="black").pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry.pack(pady=5)

gender_var = tk.StringVar(value="Other")
gender_frame = tk.Frame(root, bg="black")
tk.Label(gender_frame, text="Gender:", font=("Helvetica", 12), fg="white", bg="black").pack(side="left")

for g in ["Male", "Female", "Other"]:
    tk.Radiobutton(gender_frame, text=g, variable=gender_var, value=g,
                   font=("Helvetica", 11), fg="white", bg="black", selectcolor="red").pack(side="left", padx=5)
gender_frame.pack(pady=10)

tk.Button(root, text="Reveal My Doom", command=calculate_death,
          font=("Helvetica", 13), bg="darkred", fg="white").pack(pady=20)

output = tk.Label(root, text="", font=("Helvetica", 12), fg="lightgreen", bg="black", wraplength=400, justify="center")
output.pack(pady=10)

root.mainloop()
