from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [random.choice(letters) for letter in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for number in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if website_input.get() == "" or password_input.get() == "" or username_input.get() == "":
        messagebox.showerror(title="Error", message="Don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(),
                                       message=f"These are the details entered: \nE-mail: {username_input.get()} \nPassword: {password_input.get()} \nDo you want to save?")
        if is_ok:
            with open("passwords.txt", "r") as pw_read:
                content = pw_read.read()
                if website_input.get() in content:
                    if username_input.get() in content:
                        return None
                    else:
                        with open("passwords.txt", "a") as pw:
                            pw.writelines(f"{website_input.get()} | {username_input.get()} | {password_input.get()}\n")
                else:
                    with open("passwords.txt", "a") as pw:
                        pw.writelines(f"{website_input.get()} | {username_input.get()} | {password_input.get()}\n")
                website_input.delete(0, "end")
                password_input.delete(0, "end")
                website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PahlawanJoey's Password Manager")
window.config(padx=40, pady=20, bg="white")
bg_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=1, row=0)
# Text labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
username_label = Label(text="E-mail / Username:", bg="white")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)
# Text input
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
username_input.insert(0, "PahlawanJoey@GOAT.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")
# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
