from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk()

root.geometry('450x650')
root.title('LOTTO!!!')
root.config(bg='#fdcb08')

looter = PhotoImage(file="lottologo2.png")
img = Label(root, image=looter)
img.place(x=0, y=0)
img.config(bg='#fdcb08')


class Loot:
    results = StringVar()
    list1var = StringVar()
    list2var = StringVar()
    list3var = StringVar()

    # lists for lotto guesses
    list1 = []
    list2 = []
    list3 = []

    def __init__(self, master):
        # labels and displays ( also labels ;) )
        self.num_lab = Label(master, bg='#fdcb08', text='Lucky Numbers:').place(x=50, y=530)
        self.num_res = Label(master, bg='#fdcb08', text='', textvariable=self.results).place(x=200, y=530)
        self.num_lab = Label(master, bg='#fdcb08', text='Set 1:').place(x=50, y=380)
        self.list1_lab = Label(master, bg='#fdcb08', text='', textvariable=self.list1var).place(x=200, y=380)
        self.num_lab = Label(master, bg='#fdcb08', text='Set 2:').place(x=50, y=410)
        self.list2_lab = Label(master, bg='#fdcb08', text='', textvariable=self.list2var).place(x=200, y=410)
        self.num_lab = Label(master, bg='#fdcb08', text='Set 3:').place(x=50, y=440)
        self.list3_lab = Label(master, bg='#fdcb08', text='', textvariable=self.list3var).place(x=200, y=440)

        # lotto buttons
        self.num1 = Button(master, text='1', width=1, bg='white', command=lambda: self.lottery(1)).place(x=10, y=170)
        self.num2 = Button(master, text='2', width=1, bg='white', command=lambda: self.lottery(2)).place(x=50, y=170)
        self.num3 = Button(master, text='3', width=1, bg='white', command=lambda: self.lottery(3)).place(x=90, y=170)
        self.num4 = Button(master, text='4', width=1, bg='white', command=lambda: self.lottery(4)).place(x=130, y=170)
        self.num5 = Button(master, text='5', width=1, bg='white', command=lambda: self.lottery(5)).place(x=170, y=170)
        self.num6 = Button(master, text='6', width=1, bg='white', command=lambda: self.lottery(6)).place(x=210, y=170)
        self.num7 = Button(master, text='7', width=1, bg='white', command=lambda: self.lottery(7)).place(x=250, y=170)
        self.num8 = Button(master, text='8', width=1, bg='white', command=lambda: self.lottery(8)).place(x=290, y=170)
        self.num9 = Button(master, text='9', width=1, bg='white', command=lambda: self.lottery(9)).place(x=330, y=170)
        self.num10 = Button(master, text='10', width=1, bg='white', command=lambda: self.lottery(10)).place(x=370, y=170)
        self.num11 = Button(master, text='11', width=1, bg='white', command=lambda: self.lottery(11)).place(x=410, y=170)
        self.num12 = Button(master, text='12', width=1, bg='white', command=lambda: self.lottery(12)).place(x=10, y=210)
        self.num13 = Button(master, text='13', width=1, bg='white', command=lambda: self.lottery(13)).place(x=50, y=210)
        self.num14 = Button(master, text='14', width=1, bg='white', command=lambda: self.lottery(14)).place(x=90, y=210)
        self.num15 = Button(master, text='15', width=1, bg='white', command=lambda: self.lottery(15)).place(x=130, y=210)
        self.num16 = Button(master, text='16', width=1, bg='white', command=lambda: self.lottery(16)).place(x=170, y=210)
        self.num17 = Button(master, text='17', width=1, bg='white', command=lambda: self.lottery(17)).place(x=210, y=210)
        self.num18 = Button(master, text='18', width=1, bg='white', command=lambda: self.lottery(18)).place(x=250, y=210)
        self.num19 = Button(master, text='19', width=1, bg='white', command=lambda: self.lottery(19)).place(x=290, y=210)
        self.num20 = Button(master, text='20', width=1, bg='white', command=lambda: self.lottery(20)).place(x=330, y=210)
        self.num21 = Button(master, text='21', width=1, bg='white', command=lambda: self.lottery(21)).place(x=370, y=210)
        self.num22 = Button(master, text='22', width=1, bg='white', command=lambda: self.lottery(22)).place(x=410, y=210)
        self.num23 = Button(master, text='23', width=1, bg='white', command=lambda: self.lottery(23)).place(x=10, y=250)
        self.num24 = Button(master, text='24', width=1, bg='white', command=lambda: self.lottery(24)).place(x=50, y=250)
        self.num25 = Button(master, text='25', width=1, bg='white', command=lambda: self.lottery(25)).place(x=90, y=250)
        self.num26 = Button(master, text='26', width=1, bg='white', command=lambda: self.lottery(26)).place(x=130, y=250)
        self.num27 = Button(master, text='27', width=1, bg='white', command=lambda: self.lottery(27)).place(x=170, y=250)
        self.num28 = Button(master, text='28', width=1, bg='white', command=lambda: self.lottery(28)).place(x=210, y=250)
        self.num29 = Button(master, text='29', width=1, bg='white', command=lambda: self.lottery(29)).place(x=250, y=250)
        self.num30 = Button(master, text='30', width=1, bg='white', command=lambda: self.lottery(30)).place(x=290, y=250)
        self.num31 = Button(master, text='31', width=1, bg='white', command=lambda: self.lottery(31)).place(x=330, y=250)
        self.num32 = Button(master, text='32', width=1, bg='white', command=lambda: self.lottery(32)).place(x=370, y=250)
        self.num33 = Button(master, text='33', width=1, bg='white', command=lambda: self.lottery(33)).place(x=410, y=250)
        self.num34 = Button(master, text='34', width=1, bg='white', command=lambda: self.lottery(34)).place(x=10, y=290)
        self.num35 = Button(master, text='35', width=1, bg='white', command=lambda: self.lottery(35)).place(x=50, y=290)
        self.num36 = Button(master, text='36', width=1, bg='white', command=lambda: self.lottery(36)).place(x=90, y=290)
        self.num37 = Button(master, text='37', width=1, bg='white', command=lambda: self.lottery(37)).place(x=130, y=290)
        self.num38 = Button(master, text='38', width=1, bg='white', command=lambda: self.lottery(38)).place(x=170, y=290)
        self.num39 = Button(master, text='39', width=1, bg='white', command=lambda: self.lottery(39)).place(x=210, y=290)
        self.num40 = Button(master, text='40', width=1, bg='white', command=lambda: self.lottery(40)).place(x=250, y=290)
        self.num41 = Button(master, text='41', width=1, bg='white', command=lambda: self.lottery(41)).place(x=290, y=290)
        self.num42 = Button(master, text='42', width=1, bg='white', command=lambda: self.lottery(42)).place(x=330, y=290)
        self.num43 = Button(master, text='43', width=1, bg='white', command=lambda: self.lottery(43)).place(x=370, y=290)
        self.num44 = Button(master, text='44', width=1, bg='white', command=lambda: self.lottery(44)).place(x=410, y=290)
        self.num45 = Button(master, text='45', width=1, bg='white', command=lambda: self.lottery(45)).place(x=10, y=330)
        self.num46 = Button(master, text='46', width=1, bg='white', command=lambda: self.lottery(46)).place(x=50, y=330)
        self.num47 = Button(master, text='47', width=1, bg='white', command=lambda: self.lottery(47)).place(x=90, y=330)
        self.num48 = Button(master, text='48', width=1, bg='white', command=lambda: self.lottery(48)).place(x=130, y=330)
        self.num49 = Button(master, text='49', width=1, bg='white', command=lambda: self.lottery(49)).place(x=170, y=330)

        # buttons
        self.clr_btn = Button(master, bg='white', text='Clear', command=self.clear).place(x=270, y=580)
        self.exit = Button(master, bg='white', text='Exit', command=self.kill).place(x=130, y=580)
        self.prize = Button(master, bg='white', text='PLAY!', command=self.lotto_res).place(x=200, y=480)

    def lottery(self, num):
        if len(self.list1) < 6 and num not in self.list1:
            self.list1.append(num)
            self.list1var.set(self.list1)

        elif len(self.list1) == 6 and len(self.list2) < 6 and num not in self.list2:
            self.list2.append(num)
            self.list2var.set(self.list2)

        elif len(self.list2) == 6 and len(self.list3) < 6 and num not in self.list3:
            self.list3.append(num)
            self.list3var.set(self.list3)

    def lotto_res(self):
        global win
        y = 0
        lotto_nums = random.sample(range(1, 50), 6)
        self.results.set(lotto_nums)
        for x in range(0, 6):
            if self.list1[x] == lotto_nums[x]:
                y += 1
        if y == 6:
            win = 10000000
        elif y == 5:
            win = 8584
        elif y == 4:
            win = 2384
        elif y == 3:
            win = 100.50
        elif y == 2:
            win = 20
        elif y < 2:
            win = 0
        messagebox.showinfo("Status set 1", "Set had: " + str(y))
        messagebox.showinfo("Lotto set 1", "Numbers are: " + str(lotto_nums))
        messagebox.showinfo("Winnings set 1", "You have won R" + str(win))

        for x in range(0, 6):
            if self.list2[x] == lotto_nums[x]:
                y += 1
        if y == 6:
            win = 10000000
        elif y == 5:
            win = 8584
        elif y == 4:
            win = 2384
        elif y == 3:
            win = 100.50
        elif y == 2:
            win = 20
        elif y < 2:
            win = 0
        messagebox.showinfo("Status set 2", "Set had: " + str(y))
        messagebox.showinfo("Lotto set 2", "Numbers are: " + str(lotto_nums))
        messagebox.showinfo("Winnings set 2", "You have won R" + str(win))

        for x in range(0, 6):
            if self.list3[x] == lotto_nums[x]:
                y += 1
        if y == 6:
            win = 10000000
        elif y == 5:
            win = 8584
        elif y == 4:
            win = 2384
        elif y == 3:
            win = 100.50
        elif y == 2:
            win = 20
        elif y < 2:
            win = 0
        messagebox.showinfo("Status set 3", "Set had: " + str(y))
        messagebox.showinfo("Lotto set 3", "Numbers are: " + str(lotto_nums))
        messagebox.showinfo("Winnings set 3", "You have won R" + str(win))

    def kill(self):
        root.destroy()

    def clear(self):
        self.results.set('')


a = Loot(root)
root.mainloop()
