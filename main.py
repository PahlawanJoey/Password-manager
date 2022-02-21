from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- FIND PASSWORD  ------------------------------- #
def find_password():
    try:
        with open("passwords.json") as data:
            pw = json.load(data)
            pw = {k.lower(): v for k, v in pw.items()}
            if website_input.get().lower() in pw:
                messagebox.showinfo(title=website_input.get().title(),
                                    message=f"E-mail: {pw[website_input.get().lower()]['email']}\nPassword: {pw[website_input.get().lower()]['password']}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No details for the website exists")


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
    new_data = {
        website_input.get(): {
            "email": username_input.get(),
            "password": password_input.get(),
        }
    }
    if website_input.get() == "" or password_input.get() == "" or username_input.get() == "":
        messagebox.showerror(title="Error", message="Don't leave any fields empty")
    if website_input.get() != "" and password_input.get() != "" and username_input.get() != "":
        try:
            with open("passwords.json", "r") as pw_read:
                content = json.load(pw_read)
            if website_input.get() in content:
                if username_input.get() in content[website_input.get()]["email"]:
                    messagebox.showerror(title="Error", message="Website and E-mail combination already exists")
            else:
                content.update(new_data)
                with open("passwords.json", "w") as pw_new:
                    json.dump(content, pw_new, indent=4)
        except FileNotFoundError:
            with open("passwords.json", "w") as pw:
                json.dump(new_data, pw, indent=4)
        except json.decoder.JSONDecodeError:
            with open("passwords.json", "w") as pw:
                json.dump(new_data, pw, indent=4)
        finally:
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
website_input = Entry(width=21)
website_input.grid(column=1, row=1, sticky="EW")
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
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
