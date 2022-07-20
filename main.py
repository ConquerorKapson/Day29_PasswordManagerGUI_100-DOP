from tkinter import *


# ===================FUNCTIONALITY=========================
def destroy_window(win):
    win.quit()


def open_popup(entry):
    top = Toplevel(window)
    top.config(padx=20, pady=20)
    # top.geometry("250x100")
    top.title("Empty Password")
    Label(top, text=f"your {entry} is empty! \n \n please fill in that first", padx=20, pady=20).grid(row=0, column=0)
    ok_button = Button(top, text="ok")
    ok_button.grid(row=1, column=0)





def add_to_file():
    if website_entry.index("end") == 0:
        open_popup("website")
    elif email_entry.index("end") == 0:
        open_popup("email")
    elif password_entry.index("end") == 0:
        open_popup("password")
    else:
        with open(file="password.txt", mode='a+') as passwords:
            passwords.write(f"{website_entry.get()}   |  {email_entry.get()}   |  {password_entry.get()} \n")



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

email = Label(text="Email")
email.grid(row=2, column=0, padx=10, pady=5)

email_entry = Entry()
email_entry.grid(row=2, column=1, padx=10, pady=5)

password = Label(text="Password")
password.grid(row=3, column=0, padx=10, pady=5)

password_entry = Entry()
password_entry.grid(row=3, column=1, padx=10, pady=5)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, pady=5)

add_button = Button(text="Add", command=add_to_file)
add_button.grid(row=4, column=1, pady=5)

window.mainloop()
