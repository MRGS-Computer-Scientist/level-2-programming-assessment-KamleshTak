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

        self.create_main_page()

    def create_main_page(self):
        self.clear_window()
        
        # Creating top navigation bar
        top_nav = tk.Frame(self, bg="black", height=70)  # Increased height for larger buttons
        top_nav.pack(fill="x")

        # Adding buttons to the top navigation bar with larger fonts
        menu_button = tk.Button(top_nav, text="☰", bg="black", fg="white", borderwidth=0, font=("Helvetica", 20))
        menu_button.pack(side="left", padx=20)  # Increased padding

        home_button = tk.Button(top_nav, text="🏠", bg="black", fg="white", borderwidth=0, font=("Helvetica", 20))
        home_button.pack(side="left")

        profile_button = tk.Button(top_nav, text="👤", bg="black", fg="white", borderwidth=0, font=("Helvetica", 20), command=self.show_login_page)
        profile_button.pack(side="right", padx=20)  # Increased padding

        # Title
        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(pady=10)
        title_label = tk.Label(title_frame, text="FIT TRACK", font=("Helvetica", 24), bg="green", fg="black")
        title_label.pack()

    def show_login_page(self):
        self.clear_window()
        LoginPage(self)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(pady=10)
        title_label = tk.Label(title_frame, text="Login", font=("Helvetica", 24), bg="green", fg="black")
        title_label.pack()

        login_frame = tk.Frame(self, bg="green")
        login_frame.pack(pady=10)

        tk.Label(login_frame, text="Username:", bg="green", fg="black").grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(login_frame, text="Password:", bg="green", fg="black").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        login_button = tk.Button(login_frame, text="Login", command=self.login)
        login_button.grid(row=2, columnspan=2, pady=10)

        back_button = tk.Button(login_frame, text="Back", command=self.go_back)
        
