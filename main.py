from json import JSONDecodeError
from tkinter import *
import random
import array
import json
from tkinter import messagebox
import pyperclip

# ================GLOBAL================
LABEL_FONT = ("Helvetica", 12, "bold")
ENTRY_FONT = ("Courier New Greek", 12)
BUTTON_FONT = ("Courier New Greek", 11)
MESSAGE_FONT = ("Courier New Greek", 11)


# ===================FUNCTIONALITY=========================

def copy_to_clipboard(password):
    pyperclip.copy(password)


def open_error_popup(entry):
    messagebox.showwarning(title="Missing entry", message=f"your {entry} is empty! \n \n please fill in that first")


def verified():
    return True


def check_for_empty_search_entries():
    if website_entry.index("end") == 0:
        open_error_popup("website")
        return False
    elif email_entry.index("end") == 0:
        open_error_popup("email")
        return False
    else:
        return True


def find_password():
    if verified():
        if check_for_empty_search_entries():
            try:
                with open("password.json", 'r') as passwords:
                    all_data = json.load(passwords)
                    your_password = all_data[f"{website_entry.get().lower()},{email_entry.get().lower()}"]['Password']
                    messagebox.showinfo(
                        message=f"Your Password is : \n\n   {your_password} \n\nIt is copied to clipboard")
                    copy_to_clipboard(your_password)
            except JSONDecodeError:
                messagebox.showinfo(message="Password for these entries does not exist")
            except KeyError:
                messagebox.showinfo(message="Password for these entries does not exist")
            except FileNotFoundError:
                messagebox.showinfo(message="There is no password added into your system")


def add_to_file():
    # creating json object
    new_data = {
        f"{website_entry.get().lower()},{email_entry.get().lower()}": {
            "Website": website_entry.get(),
            "Email": email_entry.get(),
            "Password": password_entry.get()
        }
    }
    try:
        with open(file="password.json", mode='r') as fetch_passwords:
            data = json.load(fetch_passwords)
            data.update(new_data)
        with open(file="password.json", mode='w') as put_passwords:
            json.dump(data, put_passwords, indent=4)
    except FileNotFoundError:
        with open(file="password.json", mode='w') as put_passwords:
            json.dump(new_data, put_passwords, indent=4)
    except JSONDecodeError:
        with open(file="password.json", mode='w') as put_passwords:
            json.dump(new_data, put_passwords, indent=4)


def confirm_entry_popup():
    ok = False
    website_local = website_entry.get()
    email_local = email_entry.get()
    password_local = password_entry.get()
    try:
        with open(file="password.json", mode='r') as fetch_passwords:
            data = json.load(fetch_passwords)
            val = data[f"{website_local.lower()},{email_local.lower()}"]
            confirm_message = (f"Your password for website: {website_local}\n"
                               f"and email/username: {email_local} \nalready exists. "
                               f"Do you want to update the password?")

            ok = messagebox.askokcancel(title="Update?", message=confirm_message)
    except FileNotFoundError:
        with open(file="password.json", mode='w') as put_passwords:
            confirm_message = (f"your website is :{website_local} \n "
                               f"your email/username is :{email_local} \n"
                               f"your password is :{password_local} \n"
                               f"Do you want to add these?\n")
            ok = messagebox.askokcancel(title="Confirmation", message=confirm_message)
    except (JSONDecodeError, KeyError):
        confirm_message = (f"your website is :{website_local} \n "
                           f"your email/username is :{email_local} \n"
                           f"your password is :{password_local} \n"
                           f"Do you want to add these?\n")

        ok = messagebox.askokcancel(title="Confirmation", message=confirm_message)
    finally:
        if ok:
            add_to_file()


def check_for_empty_entries():
    if website_entry.index("end") == 0:
        open_error_popup("website")
    elif email_entry.index("end") == 0:
        open_error_popup("email")
    elif password_entry.index("end") == 0:
        open_error_popup("password")
    else:
        confirm_entry_popup()


def generate_password():
    MAX_LEN = 12

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    copy_to_clipboard(password_entry.get())


# ==========================UI================================


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(window, width=200, height=200, background='white')
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, padx=(0, 80))

website = Label(text="Website :", font=LABEL_FONT)
website.grid(row=1, column=0, sticky=E, pady=10)
email = Label(text="Email :", font=LABEL_FONT)
email.grid(row=2, column=0, sticky=E, pady=(0, 10))
password = Label(text="Password :", font=LABEL_FONT)
password.grid(row=3, column=0, sticky=E, pady=(0, 10))

website_entry = Entry(width=60, font=ENTRY_FONT)
website_entry.grid(row=1, column=1, sticky=W + E)
email_entry = Entry(width=50, font=ENTRY_FONT)
email_entry.grid(row=2, column=1, sticky=W)
password_entry = Entry(width=40, font=ENTRY_FONT)
password_entry.grid(row=3, column=1, sticky=W, columnspan=1)

search_password_button = Button(text="Search", font=BUTTON_FONT, command=find_password)
search_password_button.grid(row=2, column=1, sticky=E)
generate_password_button = Button(text="Generate Password", font=BUTTON_FONT, command=generate_password)
generate_password_button.grid(row=3, column=1, sticky=E)
add_button = Button(text="Add", width=30, bg="dark grey", fg="white", font=BUTTON_FONT, command=check_for_empty_entries)
add_button.grid(row=4, column=1, pady=(20, 0))

window.mainloop()
