import tkinter as tk
from PIL import Image, ImageTk

import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# game window setup

root = tk.Tk()
root.title("sleepover secrets...")
root.geometry("600x500")
root.configure(bg="#f7eefc")
root.resizable(False, False)

scene_frame = tk.Frame(root, bg="#f7eefc")
scene_frame.pack(fill="both", expand=True)

# game state

game_state = {
    "suspicion": 0
}

# clear screen

def clear_screen():
    for widget in scene_frame.winfo_children():
        widget.destroy()

# buttons

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

# character image

def show_character(path):
    img = Image.open(path)
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)

    label = tk.Label(scene_frame, image=img, bg="#f7eefc")
    label.image = img
    label.pack(pady=10)

# dialogue box

def create_dialogue_box():
    frame = tk.Frame(scene_frame, bg="#f7eefc")
    frame.pack(side="bottom", fill="x", pady=20)

    label = tk.Label(
        frame,
        text="",
        font=("Helvetica", 14),
        bg="#ffffff",
        fg="#3b2f4a",
        wraplength=560,
        padx=20,
        pady=20,
        justify="left"
    )
    label.pack()

    return label

# typing effect

def type_text(label, text, i=0):
    if i <= len(text):
        label.config(text=text[:i])
        root.after(25, lambda: type_text(label, text, i + 1))

# scenes

def intro_scene():
    clear_screen()

    game_state["suspicion"] = 0

    title = tk.Label(scene_frame, text="sleepover secrets...",
                     font=("Helvetica", 26, "bold"), bg="#f7eefc", fg="#3b2f4a")
    title.pack(pady=40)

    make_button("start sleepover ▶", room_scene).pack(pady=20)

# main room

def room_scene():
    clear_screen()

    dialogue = create_dialogue_box()
    type_text(dialogue,
              "you walk into the sleepover...\n"
              "fairy lights glow softly\n"
              "but something feels... off.")

    make_button("look around", look_scene).pack(pady=5)
    make_button("talk to your friend", talk_scene).pack(pady=5)
    make_button("check hallway", hallway_scene).pack(pady=5)

# look around

def look_scene():
    clear_screen()
    game_state["suspicion"] += 1

    dialogue = create_dialogue_box()
    type_text(dialogue,
              "the lights flicker...\n"
              "you feel like you're being watched.")

    make_button("go back", room_scene).pack(pady=10)

# hallway

def hallway_scene():
    clear_screen()
    game_state["suspicion"] += 1

    dialogue = create_dialogue_box()
    type_text(dialogue,
              "the hallway is dark...\n"
              "you hear something behind you.")

    make_button("run back", room_scene).pack(pady=5)
    make_button("keep going", shadow_scene).pack(pady=5)

# shadow encounter

def shadow_scene():
    clear_screen()

    dialogue = create_dialogue_box()

    if game_state["suspicion"] >= 3:
        type_text(dialogue,
                  "you see a shadow move...\n"
                  "it's not your friend.\n"
                  "something is here.")
        make_button("face it", bad_ending).pack(pady=5)
    else:
        type_text(dialogue,
                  "you get scared and run back.")
        make_button("go back", room_scene).pack(pady=5)

# talk to friend

def talk_scene():
    clear_screen()

    show_character(resource_path("assets/friend.png"))

    dialogue = create_dialogue_box()
    type_text(dialogue,
              "your friend smiles...\n"
              "but it feels fake.")

    make_button("ask what's wrong", suspicious_scene).pack(pady=5)
    make_button("ignore it", ignore_scene).pack(pady=5)

# suspicious

def suspicious_scene():
    clear_screen()
    game_state["suspicion"] += 1

    show_character(resource_path("assets/friend.png"))

    dialogue = create_dialogue_box()
    type_text(dialogue,
              "she hesitates...\n"
              "'it's nothing...'")

    make_button("press her", truth_scene).pack(pady=5)
    make_button("back off", room_scene).pack(pady=5)

# ignore

def ignore_scene():
    clear_screen()

    dialogue = create_dialogue_box()
    type_text(dialogue,
              "you ignore the feeling...\n"
              "maybe it's all in your head.")

    make_button("continue night", normal_ending).pack(pady=10)

# truth reveal

def truth_scene():
    clear_screen()

    show_character(resource_path("assets/friend.png"))

    dialogue = create_dialogue_box()

    if game_state["suspicion"] >= 3:
        type_text(dialogue,
                  "she whispers...\n"
                  "'someone else is in the house.'")

        make_button("investigate", brave_ending).pack(pady=5)
    else:
        type_text(dialogue,
                  "she laughs it off...\n"
                  "you feel unsure.")

        make_button("go back", room_scene).pack(pady=5)

# ---------------- endings ----------------

# normal

def normal_ending():
    clear_screen()

    dialogue = create_dialogue_box()
    type_text(dialogue,
              "the night continues normally...\n"
              "maybe nothing was wrong.\n\nEND: normal ending")

    make_button("restart", intro_scene).pack(pady=20)

# brave

def brave_ending():
    clear_screen()

    dialogue = create_dialogue_box()
    type_text(dialogue,
              "you both walk into the dark...\n"
              "ready to face whatever is there.\n\nEND: brave ending")

    make_button("restart", intro_scene).pack(pady=20)

# bad

def bad_ending():
    clear_screen()

    dialogue = create_dialogue_box()
    type_text(dialogue,
              "the shadow moves closer...\n"
              "you shouldn't have come here.\n\nEND: bad ending")

    make_button("restart", intro_scene).pack(pady=20)

# start the gameeee

intro_scene()
root.mainloop()