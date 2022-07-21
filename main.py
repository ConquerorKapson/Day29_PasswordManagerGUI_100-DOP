from tkinter import *
import random
import array

# ===================FUNCTIONALITY=========================


with open(file="password.txt", mode='a+') as password_file:
    pass


def redundant():
    is_redundant = False
    password_file = open("password.txt")

    if f"{website_entry.get() :30}   |  {email_entry.get():30}" in password_file.read():
        is_redundant = True
    password_file.close()

    return is_redundant


def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())


def open_error_popup(entry):
    top = Toplevel(window)
    top.config(padx=20, pady=20)
    top.title(f"Empty {entry}")
    Label(top, text=f"your {entry} is empty! \n \n please fill in that first").grid(row=0, column=0)
    ok_button = Button(top, text="ok", height=1, width=10, command=top.destroy)
    ok_button.grid(row=1, column=0, padx=10, pady=20)


def add_to_file():
    with open(file="password.txt", mode='a+') as passwords:
        passwords.write(
            f"{website_entry.get() :30}   |  {email_entry.get():30}   |  {password_entry.get():30} \n")


def update_file():
    test = f"{website_entry.get() :30}   |  {email_entry.get():30}"
    password_file = open(file="password.txt", mode="r")
    lines = password_file.readlines()
    password_file.close()

    for line in lines:

        if test in line:
            index = lines.index(line)
            lines[index] = f"{website_entry.get() :30}   |  {email_entry.get():30}   |  {password_entry.get():30} \n"
            password_file = open(file="password.txt", mode="w+")
            password_file.truncate(0)
            password_file.writelines(lines)
            password_file.close
            break


def confirm_entry_popup():
    if not redundant():
        def answer_is_yes():
            add_to_file()
            top.destroy()

        def answer_is_no():
            top.destroy()

        top = Toplevel(window)
        top.config(padx=20, pady=20)

        confirm_message = Label(top, text=f"your website is :{website_entry.get()} \n "
                                          f"your email/username is :{email_entry.get()} \n"
                                          f"your password is :{password_entry.get()} \n"
                                          f"Do you want to add these?\n")
        confirm_message.grid(row=0, column=1, padx=20, pady=20)

        yes_button = Button(top, text="Yes", height=1, width=20, command=answer_is_yes)
        yes_button.grid(row=1, column=0)

        no_button = Button(top, text="No", height=1, width=20, command=answer_is_no)
        no_button.grid(row=1, column=2)
    else:
        def answer_is_yes():
            update_file()
            top.destroy()

        def answer_is_no():
            top.destroy()

        top = Toplevel(window)
        top.config(padx=20, pady=20)

        confirm_message = Label(top, text=f"Your password for website: {website_entry.get()}\n"
                                          f"and email/username: {email_entry.get()} already exists\n"
                                          f"Do you want to update the password?")
        confirm_message.grid(row=0, column=1, padx=20, pady=20)

        yes_button = Button(top, text="Yes", height=1, width=20, command=answer_is_yes)
        yes_button.grid(row=1, column=0)

        no_button = Button(top, text="No", height=1, width=20, command=answer_is_no)
        no_button.grid(row=1, column=2)
        # print("redundancy found")


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
    copy_to_clipboard()


# ==========================UI================================


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(window, width=200, height=189, background='white')
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 189 / 2, image=logo)
canvas.grid(row=0, column=1, pady=10)

website = Label(text="Website")
website.grid(row=1, column=0, padx=10, pady=5)

website_entry = Entry()
website_entry.grid(row=1, column=1, padx=10, pady=5)

email = Label(text="Email/Username")
email.grid(row=2, column=0, padx=10, pady=5)

email_entry = Entry()
email_entry.grid(row=2, column=1, padx=10, pady=5)

password = Label(text="Password")
password.grid(row=3, column=0, padx=10, pady=5)

password_entry = Entry()
password_entry.grid(row=3, column=1, padx=10, pady=5)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, pady=5)

add_button = Button(text="Add", command=check_for_empty_entries)
add_button.grid(row=4, column=1, pady=5)

window.mainloop()
