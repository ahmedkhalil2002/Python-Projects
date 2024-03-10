from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list_letters = [choice(letters) for _ in range(nr_letters)]
    password_list_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_list_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_list_symbols + password_list_letters + password_list_numbers
    shuffle(password_list)

    password = "".join(password_list)

    return password


def update_password():
    password_entry.delete(0, END)
    password_entry.insert(END, generate_password())
    pyperclip.copy(password_entry.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_b():
    website = website_entry.get()
    password = password_entry.get()
    username = username_entry.get()

    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if password_entry.get() == "":
        messagebox.showwarning(title="Oops", message="Invalid Password or username")
    else:
        try:
            with open("data.json", "r") as file:
                # Read data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # update data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated Data
                json.dump(data, file, indent=4)
        finally:
            clear()


def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- Search Password ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as file:
            data_json = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data file found")
    else:
        website_name = website_entry.get()
        for name, data in data_json.items():
            if name == website_name:
                email = data["email"]
                password = data["password"]
                messagebox.showinfo(title="title", message=f"Email: {email} \nPassword: {password}")
                return 1
        messagebox.showinfo(title="title", message=f"No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)

# Logo
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

username_label = Label(text="Username/Email")
username_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=20)
# website_entry.grid(row=1, column=1)
website_entry.place(x=95, y=200)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1)
username_entry.insert(END, "ak6791335@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)


# buttons
generate_button = Button(text="Generate Password", width=43, highlightthickness=0, command=update_password)
generate_button.grid(row=4, column=0, columnspan=2)

add_button = Button(text="Add", width=43, highlightthickness=0, command=add_b)
add_button.grid(row=5, column=0, columnspan=2)

search_button = Button(text="Search", width=10, command=find_password)
search_button.place(x=225, y=197)

window.mainloop()
