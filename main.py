import tkinter as tk

# game window setup

root = tk.Tk()
root.title("sleepover secrets...")
root.geometry("600x500")
root.configure(bg="#f7eefc")
root.resizable(False, False)

def clear_screen():
    for widget in scene_frame.winfo_children():
        widget.destroy()

current_scene = "introduction."

# UI for scenes

scene_frame = tk.Frame(root, bg="#f7eefc")
scene_frame.pack(fill="both", expand=True)


def make_button(text, command):
    return tk.Button(
        scene_frame,
        text=text,
        command=command,
        font=("Helvetica", 12),
        bg="#e8d7f1",
        fg="#3b2f4a",
        activebackground="#d6bfe6",
        relief="flat",
        padx=10,
        pady=5
    )


def intro_scene():
    clear_screen()

    title = tk.Label(
        scene_frame,
        text="sleepover secrets...",
        font=("Helvetica", 26, "bold"),
        bg="#f7eefc",
        fg="#3b2f4a"
    )
    title.pack(pady=40)

    subtitle = tk.Label(
        scene_frame,
        text="a mysterious sleepover story game",
        font=("Helvetica", 14),
        bg="#f7eefc",
        fg="#6b5b7a"
    )
    subtitle.pack(pady=10)

    start_btn = make_button("start sleepover ▶", room_scene)
    start_btn.pack(pady=20)

def room_scene():
    clear_screen()

    text = tk.Label(
        scene_frame,
        text="you arrive at the sleepover...\nsomething feels a little off.",
        font=("Helvetica", 14),
        bg="#ffffff",
        fg="#3b2f4a",
        wraplength=500,
        padx=20,
        pady=20
    )
    text.pack(pady=40)

    btn1 = make_button("look around", look_scene)
    btn1.pack(pady=10)

    btn2 = make_button("talk to your friend", talk_scene)
    btn2.pack(pady=10)

def look_scene():
    clear_screen()

    text = tk.Label(
        scene_frame,
        text="the lights flicker slightly...\nthat’s weird.",
        font=("Helvetica", 14),
        bg="#ffffff",
        fg="#3b2f4a",
        wraplength=500,
        padx=20,
        pady=20
    )
    text.pack(pady=40)

    back = make_button("go back", room_scene)
    back.pack(pady=10)

def talk_scene():
    clear_screen()

    text = tk.Label(
        scene_frame,
        text="your friend smiles...\nbut it feels forced.",
        font=("Helvetica", 14),
        bg="#ffffff",
        fg="#3b2f4a",
        wraplength=500,
        padx=20,
        pady=20
    )
    text.pack(pady=40)

    suspicious = make_button("ask what's wrong", suspicious_scene)
    suspicious.pack(pady=10)

    back = make_button("go back", room_scene)
    back.pack(pady=10)

def suspicious_scene():
    clear_screen()

    text = tk.Label(
        scene_frame,
        text="she hesitates...\n\"it's nothing. just tired...\"",
        font=("Helvetica", 14),
        bg="#ffffff",
        fg="#3b2f4a",
        wraplength=500,
        padx=20,
        pady=20
    )
    text.pack(pady=40)

    back = make_button("keep watching", room_scene)
    back.pack(pady=10)

intro_scene()

# run game

root.mainloop()