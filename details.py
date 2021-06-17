
# coded by Uthmaan Breda.

from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta
import re
import rsaidnumber
import random

root = Tk()
root.geometry('450x500')
root.title('LOGIN')

# StringVar
result = StringVar()


class Login:
    
    def __init__(self, master):
        
        self.user_lab = Label(master, text='Name:').place(x=10, y=30)
        self.user_ent = Entry(master)
        self.user_ent.place(x=150, y=30)
        self.user_ent.focus()
        self.email_lab = Label(master, text='Email:').place(x=10, y=80)
        self.email_ent = Entry(master)
        self.email_ent.place(x=150, y=80)
        self.id_lab = Label(master, text='ID Number:').place(x=10, y=130)
        self.id_ent = Entry(master)
        self.id_ent.place(x=150, y=130)
        self.results = Label(master, text='', textvariable=result).place(x=150, y=230)
        self.log_btn = Button(master, text='Login', command=self.id_info).place(x=150, y=180)
        self.exit_btn = Button(master, text='Exit').place(x=130, y=280)
        self.clr_btn = Button(master, text='Clear').place(x=230, y=280)

    def email_info(self):
        expr = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

        for i in range(len(self.email_ent.get())):
            if re.search(expr, self.email_ent.get()):
                with open("details.txt", "w+") as f:
                    f.write(self.user_ent.get())
                    f.write('\n')
                    f.write(self.email_ent.get())
                    f.write('\n')
                    f.write(self.id_ent.get())
                    f.write('\n')

            else:
                messagebox.showerror("Error", "Invalid Email")
                root.destroy()

    def id_info(self):
        self.email_info()
        id_number = rsaidnumber.parse(self.id_ent.get())
        dob = id_number.date_of_birth
        age = (datetime.today() - dob) // timedelta(365.245)

        try:
            if age >= 18:
                messagebox.showinfo('Status', 'Let\'s Play!')
                root.destroy()

            elif len(self.id_ent.get()) != 13:
                messagebox.showerror("Error", "Not a valid ID number")
                root.destroy()

            else:
                messagebox.showinfo('ERROR', 'UNDERAGE!!! GO PLAY MARBLES OUTSIDE')
                root.destroy()

        except ValueError:
            if self.id_ent.get() != int:
                messagebox.showerror("Error!!!!!!!!", "The id number MUST be Integers only")


log_win = Login(root)
root.mainloop()


# show='\u2022'
