from tkinter import *

import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pd.read_csv("data/french_words.csv")
    to_learn = og_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def nxt_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(img, image=card_img)
    canvas.itemconfigure(card_title, text="French", fill="black")
    canvas.itemconfigure(card_text, text=current_card["French"], fill="black")
    flip_timer= window.after(3000, func=flip)

def flip():
    canvas.itemconfig(img, image=back_img)
    canvas.itemconfigure(card_title, text="English", fill="white")
    canvas.itemconfigure(card_text, text=current_card["English"],fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    nxt_card()


window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526)
card_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400, 263, image=card_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1)

# Button
corss_image = PhotoImage(file="images/wrong.png")
unkown_button = Button(image=corss_image, highlightthickness=0, command=nxt_card)
unkown_button.config(bg=BACKGROUND_COLOR)
unkown_button.grid(row=2, column=0)

right_image = PhotoImage(file="images/right.png")
tick_button = Button(image=right_image,  highlightthickness=0, command=is_known)
tick_button.config(bg=BACKGROUND_COLOR)
tick_button.grid(row=2, column=2)

nxt_card()

window.mainloop()