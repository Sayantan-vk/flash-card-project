from tkinter import *
import pandas as pd
from random import choice

data_list = {}
try:
    data = pd.read_csv("./data/french_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/word_to_learn.csv")
    data_list = original_data.to_dict(orient="records")
else:
    data_list = data.to_dict(orient="records")
card = {}


def data_word():
    global card, flip_timer
    card = choice(data_list)

    random_word = card["French"]
    window.after_cancel(flip_timer)
    try:
        canvas.itemconfig(canvas_image, image=image_1)
        canvas.itemconfig(canvas_title, text="French", fill="black")
        canvas.itemconfig(canvas_word, text=random_word, fill="black")
    except NameError:
        return random_word
    flip_timer = window.after(3000, english_card)


def words_known():
    data_list.remove(card)
    new_data = pd.DataFrame(data_list)
    new_data.to_csv("./data/word_to_learn.csv", index=False)
    data_word()


def english_card():
    global card
    random_word_English = card["English"]
    canvas.itemconfig(canvas_image, image=image_2)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=random_word_English, fill="white")
    return random_word_English


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Card")
flip_timer = window.after(3000, english_card)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_1 = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=image_1)
canvas.grid(row=0, column=0, columnspan=2)

image_2 = PhotoImage(file="./images/card_back.png")
image_3 = PhotoImage(file="./images/right.png")
image_4 = PhotoImage(file="./images/wrong.png")

button_right = Button(image=image_3, highlightthickness=0, command=data_word)
button_right.grid(row=1, column=0)

button_wrong = Button(image=image_4, highlightthickness=0, command=words_known)
button_wrong.grid(row=1, column=1)
canvas_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="")

canvas_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"), text=f"{data_word()}")

window.mainloop()
