import tkinter
from tkinter import *
import random
from tkinter import messagebox
import json
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range (random.randint(8,10))]
    password_number = [random.choice(numbers) for _ in range (random.randint(2,4))]
    password_symbol = [random.choice(symbols) for _ in range (random.randint(2,4))]

    password_list = password_letter + password_number +password_symbol

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = user_entry.get()
    password = pass_entry.get()
    new_dict = {
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please enter all required information")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except (FileNotFoundError, json.JSONDecodeError):

            with open("data.json", "w") as data_file:
                json.dump(new_dict, data_file, indent=4)

        else:
            data.update(new_dict)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:

            web_entry.delete(0, END)
            pass_entry.delete(0,END)
            user_entry.delete(0, END)
            user_entry.insert(0, "example@email.com")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_password():
    website = web_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Error", message="Please enter all required information")
    else:

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        except json.JSONDecodeError:
            messagebox.showinfo(title="Error", message="The data file is empty.")

        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                pyperclip.copy(password)
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No Data for {website} Exist.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.configure(padx=50, pady=50, bg="white")



bg = PhotoImage(file = "logo.png")
canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=bg)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:",font=("Arial" , 12),bg="white")
web_label.grid(row=1, column=0)
web_label.grid(row=1, column=0)

web_entry = Entry(width=30,font=("Arial" , 12),bg="white")
web_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
web_entry.focus()

user_label = Label(text="Email/Username:",font=("Arial" , 12),bg="white")
user_label.grid(row=2, column=0)

user_entry = Entry(width=30,font=("Arial" , 12),bg="white")
user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
user_entry.insert(0,"example@email.com")

pass_label = Label(text="Password:",font=("Arial" , 12),bg="white")
pass_label.grid(row=3, column=0,)

pass_entry = Entry(width=10,font=("Arial" , 12),bg="white")
pass_entry.grid(row=3, column=1, sticky="EW")

gen_button = Button(text="Generate",bg="white",command=generate_password)
gen_button.grid(row=3, column=2,columnspan=2, sticky="EW")

add_button = Button(text="Add", width=36,bg="white",command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search",bg="white",command = search_password)
search_button.grid(row=1, column=2,columnspan=2, sticky="EW")



window.mainloop()