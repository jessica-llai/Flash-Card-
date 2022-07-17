
from tkinter import *
import pandas
import random
import time


BACKGROUND_COLOR = "#B1DDC6"
WORD_FONT = ("Ariel", 60, "bold")
LAN_FONT = ("Ariel", 40, "italic")

# read the spanish word
try:
    word_list_df = pandas.read_csv("data/new_spanish_word.csv")
except FileNotFoundError:
    old_word_list_df = pandas.read_csv("data/spanish_word.csv")
    word_list = old_word_list_df.to_dict(orient="records")
else:
    word_list = word_list_df.to_dict(orient="records")
current_card = {}


# ------------------------------------ Read Word --------------------------------------------

def change_word():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)  # recount the time
    current_card = random.choice(word_list)  # this will be updqted in the global ones
    canvas.itemconfig(card_title, text="Spanish", fill="black")  # update the word in canvas every time i clieck
    canvas.itemconfig(card_word, text=current_card['Spanish'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer=window.after(3000, func=flip_card)  #after 3000ms=3s, run the function


# ------------------------------------ Flip Card--------------------------------------------

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# ------------------------------------ Remember Progress --------------------------------------------


def is_known():
    global current_card
    word_list.remove(current_card)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/new_spanish_word", index=False)
    change_word()











# ------------------------------------ UI --------------------------------------------

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)  #after 3000ms=3s, run the function




# card
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img) # the x,y cor of the canvas should be half of the width and height
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_back_img)

# word display

card_title = canvas.create_text(400, 150, text="Title", font=LAN_FONT)  # x and y relative to the canvas
card_word = canvas.create_text(400, 263, text=f"text", font=WORD_FONT)
change_word()
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)

# button
right_img = PhotoImage(file="images/right.png")
right_button=Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=0, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=change_word)
wrong_button.grid(column=1, row=1)








window.mainloop()