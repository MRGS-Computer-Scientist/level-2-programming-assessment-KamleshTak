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
        self.configure(bg="green")

        self.create_main_content()

    def create_main_content(self):
        # Clear existing content
        for widget in self.winfo_children():
            widget.destroy()

        # Creating top navigation bar
        top_nav = tk.Frame(self, bg="black", height=50)  # Adjusted height for smaller buttons
        top_nav.pack(fill="x")

        # Adding buttons to the top navigation bar with smaller fonts
        menu_button = tk.Button(top_nav, text="☰", bg="black", fg="white", borderwidth=0, font=("Helvetica", 16))
        menu_button.pack(side="left", padx=10)  # Adjusted padding

        home_button = tk.Button(top_nav, text="🏠", bg="black", fg="white", borderwidth=0, font=("Helvetica", 16), command=self.create_main_content)
        home_button.pack(side="left")

        profile_button = tk.Button(top_nav, text="👤", bg="black", fg="white", borderwidth=0, font=("Helvetica", 16))
        profile_button.pack(side="right", padx=10)  # Adjusted padding

        # Title
        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(pady=10)
        title_label = tk.Label(title_frame, text="FIT TRACK", font=("Helvetica", 20), bg="green", fg="black")
        title_label.pack()

        # Date controls
        date_frame = tk.Frame(title_frame, bg="green")
        date_frame.pack()

        prev_day_button = tk.Button(date_frame, text="◀", bg="green", fg="black", borderwidth=0, font=("Helvetica", 12), command=self.switch_to_previous_day)
        prev_day_button.pack(side="left", padx=10)

        self.date_label = tk.Label(date_frame, text="10/6/2024", font=("Helvetica", 12), bg="green", fg="black")
        self.date_label.pack(side="left")
        self.date_label.bind("<Button-1>", self.open_calendar)

        next_day_button = tk.Button(date_frame, text="▶", bg="green", fg="black", borderwidth=0, font=("Helvetica", 12), command=self.switch_to_next_day)
        next_day_button.pack(side="left", padx=10)

        # Today's Workout Title
        workout_title_frame = tk.Frame(self, bg="green")
        workout_title_frame.pack(pady=10)

        workout_title = tk.Label(workout_title_frame, text="Today's Workout", font=("Helvetica", 16), bg="green", fg="black")
        workout_title.pack(side="left")

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
        button_frame = tk.Frame(self, bg="green")
        button_frame.pack(pady=10)

        random_workout_button = tk.Button(button_frame, text="Random Workout", command=self.load_workout, bg="grey", fg="black", font=("Helvetica", 12))
        random_workout_button.pack(side="left", padx=5)

        custom_workout_button = tk.Button(button_frame, text="Custom Workout", command=self.show_custom_workout_frame, bg="grey", fg="black", font=("Helvetica", 12))
        custom_workout_button.pack(side="left", padx=5)

        tips_button = tk.Button(button_frame, text="Tips", command=self.open_tips_window, bg="grey", fg="black", font=("Helvetica", 12))
        tips_button.pack(side="left", padx=5)

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

        add_button = tk.Button(self.custom_workout_frame, text="Add Workout", command=self.add_workout, bg="grey", fg="black")
        add_button.grid(row=2, column=0, pady=10)

        remove_button = tk.Button(self.custom_workout_frame, text="Remove Selected Workout", command=self.remove_selected_workout, bg="grey", fg="black")
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

        select_btn = tk.Button(top, text="Select Date", command=get_date, bg="green", fg="black")
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
        # Close the main window and open the tips and game window
        self.destroy()
        top = tk.Toplevel()
        top.title("Tips and Click Game")
        top.geometry("300x600")
        top.configure(bg="green")

        tips_frame = tk.Frame(top, bg="green")
        tips_frame.pack(pady=10)

        tips_label = tk.Label(tips_frame, text="Workout Tips", font=("Helvetica", 16), bg="green", fg="black")
        tips_label.pack(pady=10)

        tips = [
            "Stay hydrated throughout your workout.",
            "Warm up before starting your exercises.",
            "Focus on form over weight.",
            "Include a mix of cardio and strength training.",
            "Cool down and stretch after your workout.",
            "Keep a consistent workout schedule.",
            "Listen to your body and rest when needed."
        ]

        for tip in tips:
            tk.Label(tips_frame, text=f"- {tip}", font=("Helvetica", 12), bg="green", fg="black", wraplength=280).pack(anchor="w", padx=10, pady=5)

        click_game_frame = tk.Frame(top, bg="green")
        click_game_frame.pack(pady=10)

        click_game_label = tk.Label(click_game_frame, text="Click Game", font=("Helvetica", 16), bg="green", fg="black")
        click_game_label.pack(pady=10)

        self.click_count = 0

        def increment_counter():
            self.click_count += 1
            counter_label.config(text=f"Clicks: {self.click_count}")

        click_button = tk.Button(click_game_frame, text="Click Me!", command=increment_counter, bg="grey", fg="black", font=("Helvetica", 12))
        click_button.pack(pady=10)

        counter_label = tk.Label(click_game_frame, text=f"Clicks: {self.click_count}", font=("Helvetica", 12), bg="green", fg="black")
        counter_label.pack(pady=10)

        # Add a home button to go back to the main screen
        home_button = tk.Button(top, text="Home", command=lambda: self.reopen_main_screen(top), bg="grey", fg="black", font=("Helvetica", 12))
        home_button.pack(pady=10)

    def reopen_main_screen(self, top):
        top.destroy()
        new_app = FitTrackApp()
        new_app.mainloop()

if __name__ == "__main__":
    app = FitTrackApp()
    app.mainloop()
