import bcrypt
from tkinter import Button, Label, Tk, Entry, StringVar, FLAT
from tkinter import messagebox
from database import Database
from mainwindow import MainWindow

db = Database()
db.createTable()



class Register:
    def __init__(self):
        # wyglad okienka rejestrowania sie
        self.registerWindow = Tk()
        self.registerWindow.title("Register with Python")
        self.registerWindow.geometry("300x250")
        self.label = Label(self.registerWindow, text = "Register")
        self.label.place(x=95, y=40)

        # zmienne narazie potrzebne
        self.usernameS = StringVar()
        self.passwordS = StringVar()
        self.usernameE = Entry (
            self.registerWindow, relief=FLAT, textvariable=self.usernameS)
        self.usernameE.place(x=70, y=80)
        self.passwordE = Entry (
            self.registerWindow, show="*", relief=FLAT, textvariable=self.passwordS)
        self.passwordE.place(x=70, y=120)
        self.submit = Button(self.registerWindow,text ="Submit", pady =5, padx = 20, command=self.add)
        self.submit.place(x=100, y=150)

        #faktyczne zmienne
        self.username = self.usernameS.get()
        self.password = self.passwordS.get()
        self.salt = bcrypt.gensalt()
        self.hashed = bcrypt.hashpw(self.password.encode(), self.salt)

    #odpalanie sie rejestrowania
    def run(self):
        self.registerWindow.mainloop()

    #funckja dodawania nowych uzytkownikow
    def add(self):
        data = (self.username,)
        result = db.searchData(data)
        print(result)
        if result != 0:
            data = (self.username, self.hashed)
            db.insertData(data)
            messagebox.showinfo("Successful", "Username Was Added")
            mainwindow()
            
        else:
            messagebox.showwarning("Warning", "Username already Exists")

def mainwindow():
    mainwindowTk = MainWindow()
    mainwindowTk.run()