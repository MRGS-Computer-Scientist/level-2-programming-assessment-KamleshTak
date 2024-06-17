import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime, timedelta
from tkcalendar import Calendar
import login

class FitTrackApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the parent class (tk.Tk)
        self.width = 430
        self.height = 932  # Increased height to accommodate the larger table
        self.geometry(f"{self.width}x{self.height}")  # Set the width and height of the window
        self.resizable(False, False)  # Make the window non-resizable
        self.configure(bg="green")

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

        profile_button = tk.Button(top_nav, text="👤", bg="black", fg="white", borderwidth=0, font=("Helvetica", 20), command=self.open_profile_page)
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
        workout_title = tk.Label(self, text="Today's Workout", font=("Helvetica", 18), bg="green", fg="black")
        workout_title.pack(pady=10)

        # Workout Table with increased height
        columns = ("exercise", "sets_reps")
        self.workout_table = ttk.Treeview(self, columns=columns, show="headings", height=15)  # Increased height
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
            ("Bicycle Crunches", "3 x 20"),
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
        button_frame = tk.Frame(self, bg="green")
        button_frame.pack(pady=10)

        random_workout_button = tk.Button(button_frame, text="Random Workout", command=self.load_workout)
        random_workout_button.pack(side="left", padx=10)

        custom_workout_button = tk.Button(button_frame, text="Custom Workout", command=self.show_custom_workout_frame)
        custom_workout_button.pack(side="left", padx=10)

        # Frame for adding custom workouts (initially hidden)
        self.custom_workout_frame = tk.Frame(self, bg="green")
        self.custom_workout_frame.pack(pady=10)
        self.custom_workout_frame.pack_forget()  # Hide initially

        tk.Label(self.custom_workout_frame, text="Exercise:", bg="green", fg="black").grid(row=0, column=0)
        self.exercise_entry = tk.Entry(self.custom_workout_frame)
        self.exercise_entry.grid(row=0, column=1)

        tk.Label(self.custom_workout_frame, text="Sets x Reps:", bg="green", fg="black").grid(row=1, column=0)
        self.sets_reps_entry = tk.Entry(self.custom_workout_frame)
        self.sets_reps_entry.grid(row=1, column=1)

        add_button = tk.Button(self.custom_workout_frame, text="Add Workout", command=self.add_workout)
        add_button.grid(row=2, columnspan=2, pady=10)

        remove_button = tk.Button(self.custom_workout_frame, text="Remove Selected Workout", command=self.remove_selected_workout)
        remove_button.grid(row=3, columnspan=2, pady=10)

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

        select_btn = tk.Button(top, text="Select Date", command=get_date)
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

    def open_profile_page(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.profile_frame = tk.Frame(self, bg="green")
        self.profile_frame.pack(pady=10)

        self.is_login_mode = True

        self.create_login_form()

        self.toggle_button = tk.Button(self.profile_frame, text="Switch to Sign Up", command=self.toggle_form)
        self.toggle_button.pack(pady=10)

        back_button = tk.Button(self.profile_frame, text="Back", command=self.create_main_content)
        back_button.pack(pady=10)

    def create_login_form(self):
        for widget in self.profile_frame.winfo_children():
            widget.destroy()

        tk.Label(self.profile_frame, text="Username", bg="green", fg="black").pack(pady=5)
        self.username_entry = tk.Entry(self.profile_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.profile_frame, text="Password", bg="green", fg="black").pack(pady=5)
        self.password_entry = tk.Entry(self.profile_frame, show="*")
        self.password_entry.pack(pady=5)

        login_button = tk.Button(self.profile_frame, text="Login", command=self.check_login)
        login_button.pack(pady=10)

        self.toggle_button = tk.Button(self.profile_frame, text="Switch to Sign Up", command=self.toggle_form)
        self.toggle_button.pack(pady=10)

    def create_signup_form(self):
        for widget in self.profile_frame.winfo_children():
            widget.destroy()

        tk.Label(self.profile_frame, text="Username", bg="green", fg="black").pack(pady=5)
        self.username_entry = tk.Entry(self.profile_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.profile_frame, text="Password", bg="green", fg="black").pack(pady=5)
        self.password_entry = tk.Entry(self.profile_frame, show="*")
        self.password_entry.pack(pady=5)

        tk.Label(self.profile_frame, text="Confirm Password", bg="green", fg="black").pack(pady=5)
        self.confirm_password_entry = tk.Entry(self.profile_frame, show="*")
        self.confirm_password_entry.pack(pady=5)

        signup_button = tk.Button(self.profile_frame, text="Sign Up", command=self.check_signup)
        signup_button.pack(pady=10)

        self.toggle_button = tk.Button(self.profile_frame, text="Switch to Login", command=self.toggle_form)
        self.toggle_button.pack(pady=10)

    def toggle_form(self):
        if self.is_login_mode:
            self.create_signup_form()
            self.is_login_mode = False
        else:
            self.create_login_form()
            self.is_login_mode = True

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "password":
            tk.Label(self.profile_frame, text="Login Successful", fg="green", bg="green").pack(pady=10)
        else:
            tk.Label(self.profile_frame, text="Login Failed", fg="red", bg="green").pack(pady=10)

    def check_signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if password == confirm_password:
            tk.Label(self.profile_frame, text="Sign Up Successful", fg="green", bg="green").pack(pady=10)
        else:
            tk.Label(self.profile_frame, text="Passwords do not match", fg="red", bg="green").pack(pady=10)

if __name__ == "__main__":
    app = FitTrackApp()
    app.mainloop()
