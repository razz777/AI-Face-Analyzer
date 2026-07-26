import customtkinter as ctk
from tkinter import messagebox
import subprocess
import sys
from datetime import datetime

# ------------------------
# Theme
# ------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ------------------------
# Window
# ------------------------
app = ctk.CTk()
app.title("AI Face Analyzer")
app.geometry("600x550")
app.resizable(False, False)

# ------------------------
# Title
# ------------------------
title = ctk.CTkLabel(
    app,
    text="🤖 AI Face Analyzer",
    font=("Arial", 30, "bold")
)
title.pack(pady=(30, 5))

subtitle = ctk.CTkLabel(
    app,
    text="Age • Gender Detection System",
    font=("Arial", 16)
)
subtitle.pack(pady=(0, 25))

# ------------------------
# Status
# ------------------------
status = ctk.CTkLabel(
    app,
    text="Status : Ready ✅",
    font=("Arial", 14)
)
status.pack(pady=10)

# ------------------------
# Functions
# ------------------------
def open_webcam():
    status.configure(text="Status : Webcam Running...")
    subprocess.run([sys.executable, "main.py"])
    status.configure(text="Status : Ready ✅")


def open_image():
    status.configure(text="Status : Opening Image...")
    subprocess.run([sys.executable, "image_detect.py"])
    status.configure(text="Status : Ready ✅")


def open_video():
    status.configure(text="Status : Opening Video...")
    subprocess.run([sys.executable, "video_detect.py"])
    status.configure(text="Status : Ready ✅")


def about():
    messagebox.showinfo(
        "About",
        "AI Face Analyzer\n\n"
        "Version : 1.0\n\n"
        "Developer :\n"
        "Subham Moharana\n\n"
        "Technology Used:\n"
        "• Python\n"
        "• OpenCV\n"
        "• InsightFace\n"
        "• CustomTkinter"
    )

# ------------------------
# Buttons
# ------------------------
btn1 = ctk.CTkButton(
    app,
    text="📷 Open Webcam",
    width=300,
    height=45,
    corner_radius=12,
    command=open_webcam
)
btn1.pack(pady=10)

btn2 = ctk.CTkButton(
    app,
    text="🖼 Open Image",
    width=300,
    height=45,
    corner_radius=12,
    command=open_image
)
btn2.pack(pady=10)

btn3 = ctk.CTkButton(
    app,
    text="🎥 Open Video",
    width=300,
    height=45,
    corner_radius=12,
    command=open_video
)
btn3.pack(pady=10)

btn4 = ctk.CTkButton(
    app,
    text="ℹ️ About",
    width=300,
    height=45,
    corner_radius=12,
    command=about
)
btn4.pack(pady=10)

btn5 = ctk.CTkButton(
    app,
    text="❌ Exit",
    width=300,
    height=45,
    corner_radius=12,
    fg_color="red",
    hover_color="#8B0000",
    command=app.destroy
)
btn5.pack(pady=25)

time_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 13)
)
time_label.pack(side="bottom", pady=5)

# ------------------------
# Footer
# ------------------------
footer = ctk.CTkLabel(
    app,
    text="© 2026 Subham Moharana | AI Face Analyzer",
    font=("Arial", 12)
)
footer.pack(side="bottom", pady=15)

def update_time():
    current = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    time_label.configure(text=f"🕒 {current}")
    app.after(1000, update_time)

update_time()
app.mainloop()