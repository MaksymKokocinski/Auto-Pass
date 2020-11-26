from tkinter import Button, Label, Tk, Listbox, messagebox, ttk, Frame, Scrollbar,Entry,END,NO,RIGHT,LEFT,W,Y,X,BOTTOM,TOP
import sys
import random
import pyperclip
import bcrypt
from database import Database2

db = Database2()
db.createTable()

class MainWindow:
    def __init__(self):
        self.mw = Tk()
        self.mw.title('Main Window')
        self.mw.geometry("500x500")
        # Tworzenie ramki treeview
        self.tree_frame = Frame(self.mw)
        self.tree_frame.place(x=200, y=120)
        #Scroll do Treeview
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill = Y)
        #Tworzenie Treeview
        self.my_tree = ttk.Treeview(self.tree_frame, yscrollcommand = self.tree_scroll.set)
        # Uzywanie packa
        self.my_tree.pack()
        # Configurowanie Scrolla
        self.tree_scroll.config(command=self.my_tree.yview)
        #Definiowanie kolumn
        self.my_tree['columns'] = ("Platform", "Password")
        self.my_tree.column("#0", width = 0, stretch = NO)
        self.my_tree.column("Platform", anchor = W, width = 120)
        self.my_tree.column("Password", anchor = W, width = 120)
        # Tytuły kolumn
        self.my_tree.heading("#0",text = "", anchor = W)
        self.my_tree.heading("Platform", text = "Platform",anchor = W)
        self.my_tree.heading("Password", text="Password", anchor = W)
        # Chwilowa Data
        yt = "toufu"
        pizza = "peperoni"
        data =[
            [yt,pizza],
            ["Twitch","Julkakulka1"],
            ["Facebook","Potato"],
            ["Microsoft","Lolik"],
            ["Skype","Max1"]
        ]
        global count
        count = 0
        for record in data:
            self.my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]))
            count += 1

        self.add_frame =Frame (self.mw)
        self.add_frame.place(x=200, y=60)

        #Labels
        self.nl = Label(self.add_frame, text = "Platform")
        self.nl.grid(row = 0, column = 0)
        self.tl = Label(self.add_frame, text = "Password")
        self.tl.grid(row=0, column = 2)
        #Entry boxy
        self.platform_box = Entry(self.add_frame)
        self.platform_box.grid(row=1, column = 0)
        self.password_box = Entry(self.add_frame)
        self.password_box.grid(row=1, column = 2)
        
        self.label = Label(self.mw, text = "Welcome, here you can manage your passwords, for more info click ->")        
        self.label.place(x=40, y=30)
        #Guziki
        self.infobutton = Button(self.mw, text="Info",pady=5,padx=12,command=self.info)
        self.infobutton.place(x=420, y=20)
        self.add = Button(self.mw, text="Add One Password",pady=5,padx=22,command=self.add_record)
        self.add.place(x=40, y=80)
        self.generatekey = Button(self.mw, text="Generate Password",pady=5,padx=22,command=self.generate)
        self.generatekey.place(x=40, y=120)
        self.select = Button(self.mw, text="Select One Password",pady=5,padx=16,command=self.select_record)
        self.select.place(x=40, y=160)
        self.update = Button(self.mw, text="Save One Password",pady=5,padx=20,command=self.update_record)
        self.update.place(x=40, y=200)
        self.removeone = Button(self.mw, text="Remove One Selected",pady=5,padx=14,command=self.remove_one)
        self.removeone.place(x=40, y=240)
        self.removemany = Button(self.mw, text="Remove Many Selected",pady=5,padx=10,command=self.remove_many)
        self.removemany.place(x=40, y=280)
        self.removeall = Button(self.mw, text="Remove All Passwords",pady=5,padx=12,command=self.remove_all)
        self.removeall.place(x=40, y=320)

        self.logout = Button(self.mw, text="Log out",pady=5,padx=10,command=logout)
        self.logout.place(x=40, y=450)

    def add_record(self):#poki co dziala i dodaje do bazy danych
        global count
        self.my_tree.insert(parent='', index='end', iid=count, text="", values=(self.platform_box.get(),self.password_box.get()))
        count += 1

        addplatform=self.platform_box.get()
        addpassword=self.password_box.get()
        salt = bcrypt.gensalt()
        global hashed
        hashed = bcrypt.hashpw(addpassword.encode(), salt)

        data = (addplatform,)
        result = db.searchData(data)
        if result != 0:
            data = (addplatform,hashed)
            db.insertData(data)
            messagebox.showinfo("Successful", "Platform and Password Was Added") 
        else:
            messagebox.showwarning("Warning", "Platform already Exists, try again")
        self.platform_box.delete(0, END)
        self.password_box.delete(0, END)

    def remove_all(self):
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)

    def remove_one(self):
        self.x = self.my_tree.selection()[0]
        self.my_tree.delete(self.x)

    def remove_many(self):
        x = self.my_tree.selection()
        for record in x:
            self.my_tree.delete(record)

    def select_record(self):
        #czyszczenie przed wybraniem
        self.platform_box.delete(0, END)
        self.password_box.delete(0, END)
        #wybor linii
        self.selected = self.my_tree.focus()
        #branie wartosci
        self.values = self.my_tree.item(self.selected, 'values')
        #output do entryboxow
        self.platform_box.insert(0, self.values[0])
        self.password_box.insert(0, self.values[1])

    def update_record(self):
        #wybor linii
        selected = self.my_tree.focus()
        #zapisywanie
        self.my_tree.item(selected, text = "", values = (self.platform_box.get(),self.password_box.get()))
        #czyszczenie po
        self.platform_box.delete(0, END)
        self.password_box.delete(0, END)

    def generate(self):
        self.randompass()
        pyperclip.copy(generatedpassword)
        pyperclip.paste()

    def info(self):
        data = db.readData()
        print("data:",data)
        #messagebox.showinfo("Info","Info")
        
    def run(self):
        self.mw.mainloop()

    def randompass(self):
        self.maxlen = 10

        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

        self.smallchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 
        
        self.bigchar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O',
                'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 
        
        self.symb = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<','&','#'] 
        #laczenie wszystkich znakow
        self.allchar= self.digits + self.smallchar + self.bigchar + self.symb
        """randomdigit = random.choice(digits)
        randomsmallchar = random.choice(smallchar)
        randombigchar = random.choice(bigchar)
        randomsymbol = random.choice(symb)"""
        #robienie sie hasla
        global generatedpassword
        generatedpassword = ""
        for _ in range(self.maxlen):
            generatedpassword = generatedpassword + random.choice(self.allchar)
        self.infopassword = ("Your new password:\n"+generatedpassword+"\nCopied to clipboard!")
        messagebox.showinfo("Generated Password",self.infopassword)

def logout():
    messagebox.showinfo("Logging out","Logged out")
    sys.exit()
    
mw = MainWindow()
mw.run()