from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
import smtplib

root = Tk()

root.geometry('450x650')
root.title('Claim Prize')
root.config(bg='#fdcb08')


class Claim:
    results = StringVar()

    information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
    information_json = information.json()

    conversion_rates = information_json['conversion_rates']

    currency = []
    for i in conversion_rates.keys():
        currency.append(i)

    def __init__(self, master):
        self.wins_lab = Label(master, bg='#fdcb08', text='Your total winnings:').place(x=50, y=120)
        self.wins_res = Label(master, bg='#fdcb08', text='').place(x=200, y=120)
        self.bank_lab = Label(master, text='Bank Details', bg='#fdcb08').place(x=50, y=310)
        self.acc_name_lab = Label(master, text='Account holder:', bg='#fdcb08').place(x=10, y=350)
        self.acc_name_ent = Entry(master, bg='white')
        self.acc_name_ent.place(x=200, y=350)
        self.acc_num_lab = Label(master, text='Account Number:', bg='#fdcb08').place(x=10, y=390)
        self.acc_num_ent = Entry(master, bg='white')
        self.acc_num_ent.place(x=200, y=390)
        self.address_lab = Label(master, text='Address:', bg='#fdcb08').place(x=10, y=430)
        self.address_ent = Entry(master, bg='white')
        self.address_ent.place(x=200, y=430)
        self.sel_lab = Label(master, text='Your Bank:', bg='#fdcb08').place(x=10, y=470)
        self.option = ['ABSA', 'FNB', 'Nedbank', 'Standard Bank']  # set values for option list
        self.values = StringVar()  # set variable to keep track of option value selected
        self.values.set('Select a Bank')  # set the default value on disp. (value from list can be put using option[0])
        self.opt = OptionMenu(master, self.values, *self.option)
        self.opt.config(width=15, bg='white')
        self.opt.place(x=200, y=470)

        self.conv_to = Label(master, text='Convert to:', bg='#fdcb08').place(x=10, y=160)
        self.currency_cb = ttk.Combobox(master)
        self.currency_cb['values'] = self.currency
        self.currency_cb['state'] = 'readonly'
        self.currency_cb.set('Select Currency')
        self.currency_cb.place(x=200, y=160)

        # currency converter labels and entries
        self.amount_ent = Label(master, text='Enter Amount:', bg='#fdcb08').place(x=10, y=190)
        self.ent1 = Entry(master, bg='white')
        self.ent1.place(x=200, y=190)
        self.ent1.focus()
        self.conv_lab = Label(master, text='Converted Amount:', bg='#fdcb08').place(x=10, y=230)
        self.conv_disp = Label(master, text='', textvariable=self.results, bg='#fdcb08').place(x=200, y=230)

        self.prize = Button(master, bg='white', text='submit!', command=self.submit).place(x=200, y=510)
        self.prize = Button(master, bg='white', text='convert', command=self.perform).place(x=200, y=270)

    def convert(self, to_currency, amount):
        amount = round(amount * self.conversion_rates[to_currency], 4)
        return amount

    def perform(self):
        try:
            amount = float(self.ent1.get())
            to_curr = self.currency_cb.get()

            converted_amount = self.convert(to_curr, amount)

            self.results.set(converted_amount)
        except ValueError:
            if self.ent1 != int and self.ent1 != float:
                messagebox.showerror('Entry not valid', 'Enter numbers only')

        except requests.exceptions.ConnectionError:
            messagebox.showerror('Internet error', 'Internet Bad')
        except KeyError:
            messagebox.showerror('ERROR!!!!!!!!!!!!!!!', 'Select Currency')

    def submit(self):
        claim_info = {'Account Name': self.acc_name_ent.get(),
                      'Account Number': self.acc_num_ent.get(),
                      'Address': self.address_ent.get(),
                      'Bank:': self.values.get()}

        with open("details.txt", 'a') as f:
            for key, value in claim_info.items():
                f.write('%s:%s\n' % (key, value))
        f.close()

    # def email(self):
    #     email_line = []
    #     try:
    #         with open("Emails.txt", "a+") as w:
    #             w.write("Bank Account Name: " + str(self.bank_name.get()))
    #             w.write("\n")
    #             w.write("Bank Account Number: " + str(int(self.bank_account.get())))
    #             w.write("\n")
    #         with open("Emails.txt", "+r") as f:
    #             line = f.readline()
    #             email_line.append(line)
    #             line2 = f.read()
    #         s = smtplib.SMTP('smtp.gmail.com', 587)
    #         sender = 'lifechoiceslotto147@gmail.com'
    #         receive = str(email_line[0])
    #         password = 'lifechoices2021'
    #         s.starttls()
    #         s.login(sender, password)
    #         message = str(line2)
    #         s.sendmail(sender, receive, message)
    #         s.quit()
    #     except ValueError:
    #         if self.bank_name.get() != str:
    #             messagebox.showerror("Error", "Must be in letters or characters or strings")
    #         if self.bank_account.get() != int:
    #             messagebox.showerror("Error", "Must be in numbers")


a = Claim(root)
root.mainloop()
