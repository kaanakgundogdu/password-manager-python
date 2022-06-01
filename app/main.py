import tkinter
from tkinter import messagebox
import passwordgenerator
import pyperclip


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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {mail}\nPassword: {password}\nIs it okay to save?",
    )
    if is_ok:
        with open("passwords.txt", "a") as file:
            file.write(f"{website}| {mail} | {password}\n")
            websie_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Passwor Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tkinter.PhotoImage(file="images/logo.png")
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

genereate_password_button = tkinter.Button(
    text="Generate Password", command=generate_password)
genereate_password_button.grid(row=3, column=2, sticky="EW")
add_password_button = tkinter.Button(
    text="Add", width=36, command=save_password)
add_password_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
