<<<<<<< HEAD
from  tkinter import *
from tkinter import messagebox
import random
import string
import json
import pyperclip
from tkinter import PhotoImage
from PIL import Image, ImageTk


window = Tk()
window.title("Secure Password Manager")
window.geometry("900x600")
window.resizable(True, True)


main_frame = Frame(window)

window.configure(bg="#F5F5F5")
main_frame.configure(bg="#F5F5F5")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

main_frame.grid(row=0, column=0, pady=(50, 0))


image = Image.open("OIP.webp")
image = image.resize((100, 100))

logo = ImageTk.PhotoImage(image)

logo_label = Label(main_frame, bg="#F5F5F5", image=logo)
logo_label.grid(row=0, column=0, columnspan=3, pady=(10, 5))


heading = Label(
    main_frame,
    text = "🔐Secure Password Manager",
    font=("Arial", 18, "bold")
)
heading.grid(row=1, column=0, columnspan=3, pady=(0, 25))

Label(
    main_frame,
    bg="#F5F5F5",
    text="Website",
    font = ("Arial", 11)
    ).grid(
        row=2, 
        column=0,
        sticky = "e",
        padx=(0, 15), 
        pady=10
        )

website_entry = Entry(main_frame, width=55, font = ("Arial", 12))
website_entry.grid(
    row=2, 
    column=1, 
    padx=10, 
    pady=10
)
website_entry.focus()

Label(
    main_frame,
    bg="#F5F5F5",
    text="Username",
    font = ("Arial", 11)
    ).grid(
        row=3, 
        column=0,
        sticky = "e", 
        padx=10, 
        pady=10
    )

username_entry = Entry(main_frame, width=55, font = ("Arial", 12))
username_entry.grid(
    row=3, 
    column=1, 
    padx=10, 
    pady=10
)

Label(
    main_frame,
    bg="#F5F5F5",
    text="Password",
    font = ("Arial", 11)
    ).grid(
        row=4, 
        column=0,
        sticky = "e",
        padx=10, 
        pady=10
    )

password_entry = Entry(main_frame, width=55, show="*", font = ("Arial", 12))
password_entry.grid(
    row=4, 
    column=1, 
    padx=10, 
    pady=10
)

password_visible = False


def toggle_password():
    global password_visible

    if not password_visible:
        password_entry.config(show="")
        toggle_button.config(text="Hide")
        password_visible= True
    else:
        password_entry.config(show="*")
        toggle_button.config(text="Show")
        password_visible = False

def save_password():
    
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            "username": username,
            "password": password
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showwarning(
            title="Warning",
            message="Please fill all fields!"
        )
        return

    print(new_data)

    try:
         with open("passwords.json", "r") as file:
             data = json.load(file)

    except FileNotFoundError:
         data = {}

    if website in data:
         is_ok = messagebox.askyesno(
             title = "Website  Exists",
             message = "This website already exists.\nDo you want to update it?"
        )
         if  not is_ok:
             return
    data.update(new_data)

    with open("passwords.json", "w") as file:
            json.dump(data, file, indent = 4)

    print("saved successfully")

    messagebox.showinfo(
        title="seccess",
        message="password saved successfully"
    )
    

    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    website_entry.focus()

def search_password():
    print("search button clicked ")

    try: 
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(
            title="Error",
            message="No  data file found!"
        )
        return


    search_website = website_entry.get()
    if search_website == "":
        messagebox.showwarning(
            title="warning",
            message="please enter a website name!"
        )
        return

    print(search_website)

    if search_website in data:

        username = data[search_website]["username"]
        password = data[search_website]["password"]

        messagebox.showinfo(
            title="Password Found",
            message=f"Username: {username}\nPassword: {password}"
        )
    else:
        messagebox.showerror(
            title="Not Found",
            message="Website not found!"
    )
    
def generate_password():
    characters = string.ascii_letters + string.digits
    password=""

    for i in range(12):
        password += random.choice(characters)

    print(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            title = "Warning",
            message = "No password to copy!"
        )
        return
    
    pyperclip.copy(password)

    messagebox.showinfo(
        title = "Copied",
        message = "Password copied to clipboard!"
    )

def delete_password():
    website = website_entry.get()

    if website == "":
        messagebox.showwarning(
            title = "Warning",
            message = "Please enter a website name!"
        )
        return
    
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(
            title = "Error",
            message = "No data file found!"
        )
        return
    
    if website in data:
        confirm = messagebox.askyesno(
            title = "Delete",
            message = f"Are you sure you want to delete '{website}'?"
        )
        if confirm:
            del data[website]

            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)

            messagebox.showinfo(
                title = "Success",
                message = "Password deleted successfully!"
            )

            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

        else:
            messagebox.showerror(
                title = "Not Found",
                message = "Website not found!"
            )

main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

button_frame = Frame(main_frame)
button_frame.grid(row=5, column=0, columnspan=3, pady=20)

Button(
    button_frame,
    text="Generate Password", 
    command=generate_password,
    width=20,
    font = ("Arial", 10, "bold")
    ).grid(row=0, column=0, padx=10, pady=5)

Button(
    button_frame,
    text = "Copy",
    command = copy_password,
    width = 12,
    font = ("Arial", 10, "bold")
).grid(row=0, column=1, padx= 10, pady= 5)


Button(
    button_frame,
    text="Save", 
    command=save_password,
    width=12,
    font = ("Arial", 10, "bold")
 ).grid(row=1, column=0, padx=10, pady= 5)

Button(
    button_frame,
    text = "Delete",
    command = delete_password,
    width = 12,
    font = ("Arial", 10, "bold")
).grid(row=1, column=1, padx= 10, pady=5)

Button(
    main_frame,
    text="Search", 
    command=search_password,
    width=14,
    font = ("Arial", 10, "bold")
).grid(row=2, column=2, padx=(5, 0))


toggle_button = Button(
    main_frame,
    text =  "show",
    width = 10,
    font = ("Arial", 10, "bold"),
    command = toggle_password
)
toggle_button.grid(row=4, column=2, padx=(5, 0))
=======
from  tkinter import *
from tkinter import messagebox
import random
import string
import json
import pyperclip
from tkinter import PhotoImage
from PIL import Image, ImageTk


window = Tk()
window.title("Secure Password Manager")
window.geometry("900x600")
window.resizable(True, True)


main_frame = Frame(window)

window.configure(bg="#F5F5F5")
main_frame.configure(bg="#F5F5F5")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

main_frame.grid(row=0, column=0, pady=(50, 0))


image = Image.open("OIP.webp")
image = image.resize((100, 100))

logo = ImageTk.PhotoImage(image)

logo_label = Label(main_frame, bg="#F5F5F5", image=logo)
logo_label.grid(row=0, column=0, columnspan=3, pady=(10, 5))


heading = Label(
    main_frame,
    text = "🔐Secure Password Manager",
    font=("Arial", 18, "bold")
)
heading.grid(row=1, column=0, columnspan=3, pady=(0, 25))

Label(
    main_frame,
    bg="#F5F5F5",
    text="Website",
    font = ("Arial", 11)
    ).grid(
        row=2, 
        column=0,
        sticky = "e",
        padx=(0, 15), 
        pady=10
        )

website_entry = Entry(main_frame, width=55, font = ("Arial", 12))
website_entry.grid(
    row=2, 
    column=1, 
    padx=10, 
    pady=10
)
website_entry.focus()

Label(
    main_frame,
    bg="#F5F5F5",
    text="Username",
    font = ("Arial", 11)
    ).grid(
        row=3, 
        column=0,
        sticky = "e", 
        padx=10, 
        pady=10
    )

username_entry = Entry(main_frame, width=55, font = ("Arial", 12))
username_entry.grid(
    row=3, 
    column=1, 
    padx=10, 
    pady=10
)

Label(
    main_frame,
    bg="#F5F5F5",
    text="Password",
    font = ("Arial", 11)
    ).grid(
        row=4, 
        column=0,
        sticky = "e",
        padx=10, 
        pady=10
    )

password_entry = Entry(main_frame, width=55, show="*", font = ("Arial", 12))
password_entry.grid(
    row=4, 
    column=1, 
    padx=10, 
    pady=10
)

password_visible = False


def toggle_password():
    global password_visible

    if not password_visible:
        password_entry.config(show="")
        toggle_button.config(text="Hide")
        password_visible= True
    else:
        password_entry.config(show="*")
        toggle_button.config(text="Show")
        password_visible = False

def save_password():
    
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            "username": username,
            "password": password
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showwarning(
            title="Warning",
            message="Please fill all fields!"
        )
        return

    print(new_data)

    try:
         with open("passwords.json", "r") as file:
             data = json.load(file)

    except FileNotFoundError:
         data = {}

    if website in data:
         is_ok = messagebox.askyesno(
             title = "Website  Exists",
             message = "This website already exists.\nDo you want to update it?"
        )
         if  not is_ok:
             return
    data.update(new_data)

    with open("passwords.json", "w") as file:
            json.dump(data, file, indent = 4)

    print("saved successfully")

    messagebox.showinfo(
        title="seccess",
        message="password saved successfully"
    )
    

    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    website_entry.focus()

def search_password():
    print("search button clicked ")

    try: 
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(
            title="Error",
            message="No  data file found!"
        )
        return


    search_website = website_entry.get()
    if search_website == "":
        messagebox.showwarning(
            title="warning",
            message="please enter a website name!"
        )
        return

    print(search_website)

    if search_website in data:

        username = data[search_website]["username"]
        password = data[search_website]["password"]

        messagebox.showinfo(
            title="Password Found",
            message=f"Username: {username}\nPassword: {password}"
        )
    else:
        messagebox.showerror(
            title="Not Found",
            message="Website not found!"
    )
    
def generate_password():
    characters = string.ascii_letters + string.digits
    password=""

    for i in range(12):
        password += random.choice(characters)

    print(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            title = "Warning",
            message = "No password to copy!"
        )
        return
    
    pyperclip.copy(password)

    messagebox.showinfo(
        title = "Copied",
        message = "Password copied to clipboard!"
    )

def delete_password():
    website = website_entry.get()

    if website == "":
        messagebox.showwarning(
            title = "Warning",
            message = "Please enter a website name!"
        )
        return
    
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(
            title = "Error",
            message = "No data file found!"
        )
        return
    
    if website in data:
        confirm = messagebox.askyesno(
            title = "Delete",
            message = f"Are you sure you want to delete '{website}'?"
        )
        if confirm:
            del data[website]

            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)

            messagebox.showinfo(
                title = "Success",
                message = "Password deleted successfully!"
            )

            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

        else:
            messagebox.showerror(
                title = "Not Found",
                message = "Website not found!"
            )

main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

button_frame = Frame(main_frame)
button_frame.grid(row=5, column=0, columnspan=3, pady=20)

Button(
    button_frame,
    text="Generate Password", 
    command=generate_password,
    width=20,
    font = ("Arial", 10, "bold")
    ).grid(row=0, column=0, padx=10, pady=5)

Button(
    button_frame,
    text = "Copy",
    command = copy_password,
    width = 12,
    font = ("Arial", 10, "bold")
).grid(row=0, column=1, padx= 10, pady= 5)


Button(
    button_frame,
    text="Save", 
    command=save_password,
    width=12,
    font = ("Arial", 10, "bold")
 ).grid(row=1, column=0, padx=10, pady= 5)

Button(
    button_frame,
    text = "Delete",
    command = delete_password,
    width = 12,
    font = ("Arial", 10, "bold")
).grid(row=1, column=1, padx= 10, pady=5)

Button(
    main_frame,
    text="Search", 
    command=search_password,
    width=14,
    font = ("Arial", 10, "bold")
).grid(row=2, column=2, padx=(5, 0))


toggle_button = Button(
    main_frame,
    text =  "show",
    width = 10,
    font = ("Arial", 10, "bold"),
    command = toggle_password
)
toggle_button.grid(row=4, column=2, padx=(5, 0))
>>>>>>> df5ebbc9123754365d19972c99cfb43956c93d7f
window.mainloop()