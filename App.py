import tkinter as tk
from tkinter import ttk

class FitTrackApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the parent class (tk.Tk)
        self.width = 430
        self.height = 932
        self.configure(bg="green")

        # Creating top navigation bar
        top_nav = tk.Frame(self, bg="black", height=50)
        top_nav.pack(fill="x")

        # Adding buttons to the top navigation bar
        menu_button = tk.Button(top_nav, text="☰", bg="black", fg="white", borderwidth=0)
        menu_button.pack(side="left", padx=10)

        home_button = tk.Button(top_nav, text="🏠", bg="black", fg="white", borderwidth=0)
        home_button.pack(side="left")

        profile_button = tk.Button(top_nav, text="👤", bg="black", fg="white", borderwidth=0)
        profile_button.pack(side="right", padx=10)

        # Title
        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(pady=10)
        title_label = tk.Label(title_frame, text="FIT TRACK", font=("Helvetica", 24), bg="green", fg="black")
        title_label.pack()

        date_label = tk.Label(title_frame, text="10/6/2024", font=("Helvetica", 14), bg="green", fg="black")
        date_label.pack()

        # Today's Workout Title
        workout_title = tk.Label(self, text="Today Workout", font=("Helvetica", 18), bg="green", fg="black")
        workout_title.pack(pady=10)

        # Workout Table
        columns = ("exercise", "sets_reps")
        workout_table = ttk.Treeview(self, columns=columns, show="headings")
        workout_table.heading("exercise", text="Exercise")
        workout_table.heading("sets_reps", text="Sets x Reps")

        # Adding data to the table
        workout_data = [
            ("Squats", "3 x 10"),
            ("Push-ups", "3 x 12"),
            ("Plank", "3 x 30 seconds"),
            ("Crunches", "3 x 15")
        ]

        for exercise, sets_reps in workout_data:
            workout_table.insert("", "end", values=(exercise, sets_reps))

        workout_table.pack(pady=10)

if __name__ == "__main__":
    app = FitTrackApp()
    app.mainloop()
