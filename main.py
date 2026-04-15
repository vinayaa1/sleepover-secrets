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

    show_character("assets/friend.png")

    dialogue = create_dialogue_box(scene_frame)

    type_text(
        dialogue,
        "you walk into the sleepover...\n"
        "fairy lights glow softly, snacks everywhere\n"
        "but something feels... off."
    )

    btn1 = make_button("look around", look_scene)
    btn1.pack(pady=5)

    btn2 = make_button("talk to your friend", talk_scene)
    btn2.pack(pady=5)

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

def show_character(image_path):
    img = tk.PhotoImage(file=image_path)

    label = tk.Label(scene_frame, image=img, bg="#f7eefc")
    label.image = img
    label.pack(pady=10)

def create_dialogue_box(parent, text=""):
    frame = tk.Frame(parent, bg="#f7eefc")
    frame.pack(side="bottom", fill="x", pady=20)

    label = tk.Label(
        frame,
        text=text,
        font=("Helvetica", 14),
        bg="#ffffff",
        fg="#3b2f4a",
        wraplength=600,
        padx=20,
        pady=20,
        justify="left"
    )
    label.pack()

    return label

def type_text(label, text, i=0):
    if i <= len(text):
        label.config(text=text[:i])
        root.after(25, lambda: type_text(label, text, i + 1))

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