import json
import tkinter
from tkinter import messagebox
import passwordgenerator
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, tkinter.END)
    password = passwordgenerator.create_password()
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():

    website = websie_entry.get()
    mail = email_entry.get()
    password = password_entry.get()

    new_data = {website: {"email": mail, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
        return

    try:
        with open("app\passwords.json", "r") as data_file:
            data = json.load(data_file)
    except:
        with open("app\passwords.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("app\passwords.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        websie_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)

# ---------------------------- SEARCH ------------------------------- #


def search():
    website = websie_entry.get()

    try:
        with open("app\passwords.json", "r") as data_file:
            data = json.load(data_file)
            search_data = data[website]
            email_ = search_data["email"]
            password_ = search_data["password"]
            messagebox.showinfo(
                title="Search Results", message=f"E-mail: {email_}\nPassword: {password_}")
        return
    except:
        messagebox.showinfo(
            title="Oops", message=f"There is no site such as {website}")

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Passwor Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tkinter.PhotoImage(file="app\images\logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0, sticky="EW")
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="EW")
password_label = tkinter.Label(text="Pasword:")
password_label.grid(row=3, column=0)

websie_entry = tkinter.Entry(width=35)
websie_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
websie_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.insert(0, "kaanakgundogdu@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")


search_button = tkinter.Button(
    text="Search", command=search)
search_button.grid(row=1, column=2, sticky="EW")


genereate_password_button = tkinter.Button(
    text="Generate Password", command=generate_password)
genereate_password_button.grid(row=3, column=2, sticky="EW")
add_password_button = tkinter.Button(
    text="Add", width=36, command=save_password)
add_password_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
