from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"


# --------------- Generate Words -------------- #
# read data
data = pd.read_csv("./data/french_words.csv")

# Word Dict
# word_dict = {row.French: row.English for (index, row) in data.iterrows()}
word_list = data.to_dict(orient="records")

item = {}


# Button function
def generate_word():
    global item, flip_timer
    window.after_cancel(flip_timer)
    item = choice(word_list)  # return Dict item
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=item["French"], fill="black")
    canvas.itemconfig(card_image, image=old_image)
    flip_timer = window.after(3000, change_card)


# # change card
def change_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=item["English"], fill="white")
    canvas.itemconfig(card_image, image=new_image)


# --------------- UI -------------- #
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, change_card)
# Image card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
img = PhotoImage(file="./images/card_front.png")
card_image = canvas.create_image(405, 263, image=img)
canvas.grid(row=0, column=0, columnspan=2)
# Text
title = canvas.create_text(405, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(405, 280, text="Word", font=("Arial", 60, "bold"))

# Buttons
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_word)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="./images/wrong.png")
right_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

old_image = PhotoImage(file="./images/card_front.png")
new_image = PhotoImage(file="./images/card_back.png")


generate_word()


window.mainloop()
