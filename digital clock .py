import tkinter as tk
import customtkinter as ctk
import time
import datetime
import pyttsx3
import threading

# ------------------ TTS Engine ------------------
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ------------------ App Window ------------------
ctk.set_appearance_mode("dark")  # default = dark
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Advanced Digital Clock")
root.geometry("600x400")

# ------------------ Clock Labels ------------------
time_label = ctk.CTkLabel(root, text="", font=("Arial", 60, "bold"))
time_label.pack(pady=20)

date_label = ctk.CTkLabel(root, text="", font=("Arial", 25))
date_label.pack(pady=10)

status_label = ctk.CTkLabel(root, text="No Alarm Set", font=("Arial", 15))
status_label.pack(pady=5)

# ------------------ Alarm ------------------
alarm_time = None

def set_alarm():
    global alarm_time
    alarm_time = alarm_entry.get()
    status_label.configure(text=f"Alarm set for {alarm_time}")
    speak(f"Alarm set for {alarm_time}")

def check_alarm():
    global alarm_time
    if alarm_time:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            speak("Wake up! Your alarm is ringing!")
            status_label.configure(text="⏰ Alarm Ringing!")
            alarm_time = None
    root.after(1000, check_alarm)

# ------------------ Update Time ------------------
def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = datetime.date.today().strftime("%A, %d %B %Y")
    time_label.configure(text=current_time)
    date_label.configure(text=current_date)

    # हर घंटे बोलना
    if time.strftime("%M:%S") == "00:00":
        speak(f"The time is {time.strftime('%H')} o'clock")

    root.after(1000, update_time)

# ------------------ Widgets ------------------
frame = ctk.CTkFrame(root)
frame.pack(pady=15)

alarm_entry = ctk.CTkEntry(frame, placeholder_text="HH:MM (24-hour)", width=120)
alarm_entry.grid(row=0, column=0, padx=5)

set_btn = ctk.CTkButton(frame, text="Set Alarm", command=set_alarm)
set_btn.grid(row=0, column=1, padx=5)

theme_btn = ctk.CTkButton(frame, text="Toggle Theme", 
                          command=lambda: ctk.set_appearance_mode("light" if ctk.get_appearance_mode()=="Dark" else "dark"))
theme_btn.grid(row=0, column=2, padx=5)

footer_label = ctk.CTkLabel(root, text="Made with ❤️ in Python", font=("Arial", 12))
footer_label.pack(side="bottom", pady=10)

# ------------------ Run ------------------
update_time()
check_alarm()
root.mainloop()
