import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Global variables to track passcode and attempt counts
passcode = None
attempts = 0
max_attempts = 5
successful_attempts = 0
failed_attempts = 0

# Function to set the passcode
def set_passcode():
    global passcode
    passcode = entry.get()
    if len(passcode) == 6 and passcode.isdigit():
        entry.delete(0, tk.END)
        entry.pack_forget()
        label.config(text="Passcode set! Now try to repeat the passcode.")
        attempt_label.config(text=f"Attempt #1")
        attempt_label.pack(pady=5)
        entry2.pack(pady=10)
        set_button.pack_forget()
        check_button.pack(pady=10)
    else:
        messagebox.showerror("Error", "Please enter a valid 6-digit passcode.")

# Function to check the passcode
def check_passcode():
    global attempts, successful_attempts, failed_attempts

    if attempts < max_attempts:
        user_input = entry2.get()
        if user_input == passcode:
            successful_attempts += 1
        else:
            failed_attempts += 1
            messagebox.showinfo("Result", "Incorrect passcode.")

        attempts += 1
        entry2.delete(0, tk.END)

        if attempts < max_attempts:
            attempt_label.config(text=f"Attempt #{attempts + 1}")

        if attempts >= max_attempts:
            messagebox.showinfo("Summary", f"Attempt limit reached. Successful attempts: {successful_attempts}. Failed attempts: {failed_attempts}.")
            # Reset for a new session
            reset_app()
    else:
        messagebox.showerror("Error", "You have reached the maximum number of attempts.")

def reset_app():
    global attempts, successful_attempts, failed_attempts

    # Reset variables
    attempts = 0
    successful_attempts = 0
    failed_attempts = 0

    # Reset UI
    entry2.pack_forget()
    attempt_label.pack_forget()
    set_button.pack(pady=10)
    check_button.pack_forget()
    label.config(text="Enter a 6-digit passcode to memorize:")
    entry.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Passcode Memorization App")
root.geometry("400x400")

# Load and display padlock image as background
padlock_image = Image.open("padlock.png")  # Make sure the image is in the same directory or provide a full path
padlock_image = padlock_image.resize((400, 400), Image.LANCZOS)
padlock_photo = ImageTk.PhotoImage(padlock_image)

background_label = tk.Label(root, image=padlock_photo)
background_label.place(relwidth=1, relheight=1)

# Define style options
label_font = ("Helvetica", 14)
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")
button_bg = "#4caf50"
button_fg = "#ffffff"
set_button_fg = "#000000"  # Black color for the Set Passcode button text
check_button_fg = "#000000"  # Black color for the Check Passcode button text

# Create and pack widgets
label = tk.Label(root, text="Enter a 6-digit passcode to memorize:", font=label_font, bg='#f0f8ff')
label.pack(pady=20)

entry = tk.Entry(root, font=entry_font, justify='center')
entry.pack(pady=10)

attempt_label = tk.Label(root, text="", font=label_font, bg='#f0f8ff')
attempt_label.pack(pady=5)
attempt_label.pack_forget()

entry2 = tk.Entry(root, font=entry_font, justify='center')
entry2.pack(pady=10)
entry2.pack_forget()  # Hide initially

set_button = tk.Button(root, text="Set Passcode", font=button_font, bg=button_bg, fg=set_button_fg, command=set_passcode)
set_button.pack(pady=10)

check_button = tk.Button(root, text="Check Passcode", font=button_font, bg=button_bg, fg=check_button_fg, command=check_passcode)
check_button.pack(pady=10)
check_button.pack_forget()  # Hide initially

# Bring widgets to the front
label.lift()
entry.lift()
entry2.lift()
attempt_label.lift()
set_button.lift()
check_button.lift()

# Run the main loop
root.mainloop()
