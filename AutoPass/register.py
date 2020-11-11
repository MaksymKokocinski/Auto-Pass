import bcrypt
from tkinter import Button, Label, Tk, Entry, StringVar, FLAT, messagebox
from database import Database
from mainwindow import MainWindow

db = Database()
db.createTable()

#dodac info gdzies i guzik cofnij

class Register:
    def __init__(self):
        # wyglad okienka rejestrowania sie
        self.registerWindow = Tk()
        self.registerWindow.title("Register with Python")
        self.registerWindow.geometry("300x250")
        self.label = Label(self.registerWindow, text = "Register")
        self.label.place(x=95, y=40)

        # zmienne puste potrzebne
        global usernameS
        global passwordS
        usernameS = StringVar()
        passwordS = StringVar()
        #pola do pisania i guzik do wyslania zmiennych
        usernameE = Entry ( self.registerWindow, relief=FLAT, textvariable= usernameS)
        usernameE.place(x=70, y=80)
        passwordE = Entry ( self.registerWindow, show="*", relief=FLAT, textvariable= passwordS)
        passwordE.place(x=70, y=120)
        self.submit = Button(self.registerWindow,text ="Submit", pady =5, padx = 20, command=self.commit)
        self.submit.place(x=100, y=150)

    def commit(self):
        #zbieranie zmiennych po nacisnieciu guzika i wysylanie ich do bazy danych
        global username
        global password
        username = usernameS.get()
        password = passwordS.get()
        #print(username,password)
        salt = bcrypt.gensalt()
        global hashed
        hashed = bcrypt.hashpw(password.encode(), salt)
        self.add()

    #odpalanie sie rejestrowania
    def run(self):
        self.registerWindow.mainloop()
    #zamykanie okna rejestracji
    def quit(self):
        self.registerWindow.destroy()

    #funckja dodawania nowych uzytkownikow do bazy danych
    def add(self):
        data = (username,)
        result = db.searchData(data)
        if result != 0:
            data = (username,hashed)
            db.insertData(data)
            messagebox.showinfo("Successful", "Username Was Added")
            self.quit()
            mainwindow()  
        else:
            messagebox.showwarning("Warning", "Username already Exists, try again")

#otwieranie nastepnego okna
def mainwindow():
    mainwindowTk = MainWindow()
    mainwindowTk.run()
"""
mw = Register()
mw.run()"""