import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime, timedelta
from tkcalendar import Calendar

class FitTrackApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the parent class (tk.Tk)
        self.width = 430
        self.height = 932  # Increased height to accommodate the larger table
        self.geometry(f"{self.width}x{self.height}")  # Set the width and height of the window
        self.resizable(False, False)  # Make the window non-resizable
        self.configure(bg="lightgrey")  # Changed background color to light grey

        self.logged_in_username = None  # Store the logged-in username

        self.create_main_content()

    def create_main_content(self):
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
        title_frame = tk.Frame(self, bg="lightgrey")
        title_frame.pack(pady=10)
        title_label = tk.Label(title_frame, text="FIT TRACK", font=("Helvetica", 24), bg="lightgrey", fg="black")
        title_label.pack()

        # Date controls
        date_frame = tk.Frame(title_frame, bg="lightgrey")
        date_frame.pack()

        prev_day_button = tk.Button(date_frame, text="◀", bg="lightgrey", fg="black", borderwidth=0, font=("Helvetica", 14), command=self.switch_to_previous_day)
        prev_day_button.pack(side="left", padx=10)

        self.date_label = tk.Label(date_frame, text="10/6/2024", font=("Helvetica", 14), bg="lightgrey", fg="black")
        self.date_label.pack(side="left")
        self.date_label.bind("<Button-1>", self.open_calendar)

        next_day_button = tk.Button(date_frame, text="▶", bg="lightgrey", fg="black", borderwidth=0, font=("Helvetica", 14), command=self.switch_to_next_day)
        next_day_button.pack(side="left", padx=10)

        # Today's Workout Title
        workout_title = tk.Label(self, text="Today's Workout", font=("Helvetica", 18), bg="lightgrey", fg="black")
        workout_title.pack(pady=10)

        # Workout Table with increased height
        columns = ("exercise", "sets_reps")
        
        # Set up style
        style = ttk.Style()
        style.configure("Custom.Treeview", background="white", fieldbackground="white")
        
        self.workout_table = ttk.Treeview(self, columns=columns, show="headings", height=15, style="Custom.Treeview")  # Increased height
        self.workout_table.heading("exercise", text="Exercise")
        self.workout_table.heading("sets_reps", text="Sets x Reps")

        self.workout_table.pack(pady=10)

        # List of potential exercises
        self.workout_data = [
            ("Deadlifts", "3 x 10"),
            ("Bench Press", "3 x 12"),
            ("Shoulder Press", "3 x 10"),
            ("Bicep Curls", "3 x 15"),
            ("Tricep Dips", "3 x 12"),
            ("Pull-ups", "3 x 8"),
            ("Chin-ups", "3 x 8"),
            ("Rowing", "3 x 15"),
            ("High Knees", "3 x 30 seconds"),
            ("Butt Kicks", "3 x 30 seconds"),
            ("Side Lunges", "3 x 10"),
            ("Calf Raises", "3 x 20"),
            ("Chest Flys", "3 x 12"),
            ("Dumbbell Rows", "3 x 12"),
            ("Lat Pulldowns", "3 x 15")
        ]

        self.current_date = datetime.strptime(self.date_label.cget("text"), "%m/%d/%Y")

        # Buttons to choose between random workout and custom workout
        button_frame = tk.Frame(self, bg="lightgrey")
        button_frame.pack(pady=10)

        random_workout_button = tk.Button(button_frame, text="Random Workout", command=self.load_workout, bg="grey", fg="black", font=("Helvetica", 12))
        random_workout_button.pack(side="left", padx=10)

        custom_workout_button = tk.Button(button_frame, text="Custom Workout", command=self.show_custom_workout_frame, bg="grey", fg="black", font=("Helvetica", 12))
        custom_workout_button.pack(side="left", padx=10)

        # Tips Button
        tips_button = tk.Button(button_frame, text="Tips", command=self.open_tips_window, bg="grey", fg="black", font=("Helvetica", 12))
        tips_button.pack(side="left", padx=10)

        # Frame for adding custom workouts (initially hidden)
        self.custom_workout_frame = tk.Frame(self, bg="lightgrey")
        self.custom_workout_frame.pack(pady=10)
        self.custom_workout_frame.pack_forget()  # Hide initially

        tk.Label(self.custom_workout_frame, text="Exercise:", bg="lightgrey", fg="black").grid(row=0, column=0)
        self.exercise_entry = tk.Entry(self.custom_workout_frame)
        self.exercise_entry.grid(row=0, column=1)

        tk.Label(self.custom_workout_frame, text="Sets x Reps:", bg="lightgrey", fg="black").grid(row=1, column=0)
        self.sets_reps_entry = tk.Entry(self.custom_workout_frame)
        self.sets_reps_entry.grid(row=1, column=1)

        add_button = tk.Button(self.custom_workout_frame, text="Add Workout", command=self.add_workout, bg="grey", fg="black", font=("Helvetica", 12))
        add_button.grid(row=2, column=0, pady=10)

        remove_button = tk.Button(self.custom_workout_frame, text="Remove Selected Workout", command=self.remove_selected_workout, bg="grey", fg="black", font=("Helvetica", 12))
        remove_button.grid(row=2, column=1, pady=10)

        self.load_workout()

    def load_workout(self):
        # Clear the current table
        for item in self.workout_table.get_children():
            self.workout_table.delete(item)

        # Randomly select 10 exercises to fill the larger table
        selected_workout = random.sample(self.workout_data, 10)

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

        select_btn = tk.Button(top, text="Select Date", command=get_date, bg="lightgrey", fg="black")
        select_btn.pack(pady=20)

    def add_workout(self):
        exercise = self.exercise_entry.get()
        sets_reps = self.sets_reps_entry.get()
        if exercise and sets_reps:
            self.workout_table.insert("", "end", values=(exercise, sets_reps))
            self.exercise_entry.delete(0, tk.END)
            self.sets_reps_entry.delete(0, tk.END)

    def remove_selected_workout(self):
        selected_item = self.workout_table.selection()
        if selected_item:
            self.workout_table.delete(selected_item)

    def show_custom_workout_frame(self):
        self.custom_workout_frame.pack(pady=10)

    def open_tips_window(self):
        top = tk.Toplevel(self)
        top.geometry(f"{self.width}x{self.height}")
        top.configure(bg="lightgrey")
        top.title("Tips and Click Game")

        tips = [
            "Stay hydrated before, during, and after your workout.",
            "Warm up properly before starting your main workout.",
            "Maintain proper form to avoid injuries.",
            "Gradually increase the intensity of your workouts.",
            "Include both cardio and strength training exercises.",
            "Cool down and stretch after your workout.",
            "Keep a consistent workout schedule.",
            "Listen to your body and rest when needed."
        ]

        for tip in tips:
            tk.Label(top, text=f"- {tip}", font=("Helvetica", 12), bg="lightgrey", fg="black", wraplength=400, justify="left").pack(anchor="w", padx=20)

        # Click Game Section
        tk.Label(top, text="Click Game", font=("Helvetica", 18), bg="lightgrey", fg="black").pack(pady=10)

        self.clicks = 0
        self.start_time = None
        self.score = 0

        self.click_button = tk.Button(top, text="💧", font=("Helvetica", 16), command=self.increment_clicks)
        self.click_button.pack(pady=10)

        self.click_label = tk.Label(top, text=f"Clicks: {self.clicks}", font=("Helvetica", 14), bg="lightgrey", fg="black")
        self.click_label.pack(pady=10)

        # Score Button
        self.score_button = tk.Button(top, text=f"Score: {self.score}", font=("Helvetica", 14), bg="grey", fg="black")
        self.score_button.pack(pady=10)

        # Time Button
        self.time_button = tk.Button(top, text="Time: 0s", font=("Helvetica", 14), bg="grey", fg="black")
        self.time_button.pack(pady=10)

        # Home Button
        home_button = tk.Button(top, text="Home", command=self.reopen_main_screen, bg="grey", fg="black", font=("Helvetica", 12))
        home_button.pack(pady=10)

    def reopen_main_screen(self):
        self.deiconify()

    def increment_clicks(self):
        if self.start_time is None:
            self.start_time = datetime.now()

        self.clicks += 1
        self.click_label.config(text=f"Clicks: {self.clicks}")

        # Update score
        self.score += 10  # Assuming each click gives 10 points
        self.score_button.config(text=f"Score: {self.score}")

        # Update time
        elapsed_time = (datetime.now() - self.start_time).seconds
        self.time_button.config(text=f"Time: {elapsed_time}s")

        # Move the button to a random location within the window bounds
        x = random.randint(0, self.width - 50)
        y = random.randint(0, self.height - 50)
        self.click_button.place(x=x, y=y)

if __name__ == "__main__":
    app = FitTrackApp()
    app.mainloop()
