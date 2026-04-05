import tkinter as tk

# game window setup

root = tk.Tk()
root.title("sleepover secrets...")
root.geometry("600x500")
root.configure(bg="#f7eefc")
root.resizable(False, False)

current_scene = "introduction."

# UI for scenes

scene_frame = tk.Frame(root, bg="#f7eefc")
scene_frame.pack(fill="both", expand=True)

# title label

title = tk.Label(
    scene_frame,
    text="sleepover secrets Zzz",
    font=("Helvetica", 26, "bold"),
    bg="#f7eefc",
    fg="#6b5b7a"
)

title.pack(pady=40)

subtitle = tk.Label(
    scene_frame,
    text="a soft and mysterious sleepover story game...",
    font = ("Helvetica", 14),
    bg="#f7eefc",
    fg="6b5b7a"
)

subtitle.pack(pady=10)

# dialogue box

dialogue_box = tk.Label(
    scene_frame,
    text="",
    font=("Helvetica", 14),
    bg="#ffffff",
    fg = "#3b2f4a",
    wraplength=600,
    justify="center",
    padx=20,
    pady=20,
    relief="flat"
)

dialogue_box.pack(pady=40)

# main functions of da game


