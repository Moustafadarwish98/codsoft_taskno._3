from tkinter import *
from random import randint, choice, shuffle
import pyperclip

GREY = "#95A5A6"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    pass_in.delete(0, END)
    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)
    l_list = [choice(letters) for x in range(nr_letters)]
    n_list = [choice(numbers) for x in range(nr_numbers)]
    s_list = [choice(symbols) for x in range(nr_symbols)]
    password_list = l_list + n_list + s_list
    shuffle(password_list)
    pass_word = ''.join(password_list)
    pass_in.insert(0, pass_word)
    pyperclip.copy(pass_word)


"""Window setup"""
window = Tk()
window.config(padx=50, pady=50, bg=GREY)
window.title("Password manager.")
"""Logo"""
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=GREY)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
"""Label"""
password = Label(text="Password:", bg=GREY)
password.grid(column=0, row=3)
"""Entries"""
pass_in = Entry(width=35)
pass_in.grid(row=3, column=1)
"""Buttons"""
gen = Button(text="Generate Password", bg=GREY, command=generate_password)
gen.grid(row=3, column=2)
window.mainloop()