import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime, timedelta
from tkcalendar import Calendar

class FitTrackApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the parent class (tk.Tk)
        self.width = 430
        self.height = 832  # Decreased height to accommodate the smaller table
        self.geometry(f"{self.width}x{self.height}")  # Set the width and height of the window
        self.resizable(False, False)  # Make the window non-resizable
        self.configure(bg="green")

        # Creating top navigation bar
        top_nav = tk.Frame(self, bg="black", height=70)  # Increased height for larger buttons
        top_nav.pack(fill="x")

        # Adding buttons to the top navigation bar with larger fonts
        menu_button = tk.Button(top_nav, text="☰", bg="black", fg="white", borderwidth=0, font=("Helvetica", 20))
        menu_button.pack(side="left", padx=20)  # Increased padding

        home_button = tk.Button(top_nav, text="🏠", bg="black", fg="white", borderwidth=0, font=("Helvetica", 20))
        home_button.pack(side="left")

        profile_button = tk.Button(top_nav, text="👤", bg="black", fg="white", borderwidth=0, font=("Helvetica", 20))
        profile_button.pack(side="right", padx=20)  # Increased padding

        # Title
        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(pady=10)
        title_label = tk.Label(title_frame, text="FIT TRACK", font=("Helvetica", 24), bg="green", fg="black")
        title_label.pack()

        # Date controls
        date_frame = tk.Frame(title_frame, bg="green")
        date_frame.pack()

        prev_day_button = tk.Button(date_frame, text="◀", bg="green", fg="black", borderwidth=0, font=("Helvetica", 14), command=self.switch_to_previous_day)
        prev_day_button.pack(side="left", padx=10)

        self.date_label = tk.Label(date_frame, text="10/6/2024", font=("Helvetica", 14), bg="green", fg="black")
        self.date_label.pack(side="left")
        self.date_label.bind("<Button-1>", self.open_calendar)

        next_day_button = tk.Button(date_frame, text="▶", bg="green", fg="black", borderwidth=0, font=("Helvetica", 14), command=self.switch_to_next_day)
        next_day_button.pack(side="left", padx=10)

        # Today's Workout Title
        workout_title = tk.Label(self, text="Today Workout", font=("Helvetica", 18), bg="green", fg="black")
        workout_title.pack(pady=10)

        # Workout Table with reduced height
        columns = ("exercise", "sets_reps")
        self.workout_table = ttk.Treeview(self, columns=columns, show="headings", height=5)  # Reduced height
        self.workout_table.heading("exercise", text="Exercise")
        self.workout_table.heading("sets_reps", text="Sets x Reps")

        self.workout_table.pack(pady=10)

        # List of potential exercises
        self.workout_data = [
            ("Squats", "3 x 10"),
            ("Push-ups", "3 x 12"),
            ("Plank", "3 x 30 seconds"),
            ("Crunches", "3 x 15"),
            ("Lunges", "3 x 10"),
            ("Burpees", "3 x 12"),
            ("Mountain Climbers", "3 x 30 seconds"),
            ("Sit-ups", "3 x 15"),
            ("Jumping Jacks", "3 x 30"),
            ("Leg Raises", "3 x 12"),
            ("Russian Twists", "3 x 15"),
            ("Bicycle Crunches", "3 x 20")
        ]

        self.current_date = datetime.strptime(self.date_label.cget("text"), "%m/%d/%Y")
        self.load_workout()

    def load_workout(self):
        # Clear the current table
        for item in self.workout_table.get_children():
            self.workout_table.delete(item)

        # Randomly select 4 exercises
        selected_workout = random.sample(self.workout_data, 4)

        # Adding random data to the table
        for exercise, sets_reps in selected_workout:
            self.workout_table.insert("", "end", values=(exercise, sets_reps))

    def switch_to_previous_day(self):
        self.current_date -= timedelta(days=1)
        self.date_label.config(text=self.current_date.strftime("%m/%d/%Y"))
        self.load_workout()

    def switch_to_next_day(self):
        self.current_date += timedelta(days=1)
        self.date_label.config(text=self.current_date.strftime("%m/%d/%Y"))
        self.load_workout()

    def open_calendar(self, event):
        top = tk.Toplevel(self)
        cal = Calendar(top, selectmode='day', year=self.current_date.year, month=self.current_date.month, day=self.current_date.day)
        cal.pack(pady=20)

        def get_date():
            self.current_date = datetime.strptime(cal.get_date(), "%m/%d/%y")
            self.date_label.config(text=self.current_date.strftime("%m/%d/%Y"))
            self.load_workout()
            top.destroy()

        select_btn = tk.Button(top, text="Select Date", command=get_date)
        select_btn.pack(pady=20)

if __name__ == "__main__":
    app = FitTrackApp()
    app.mainloop()
