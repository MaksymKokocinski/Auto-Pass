'''
1. Logowanie sie do calego programu
2.od razu otwiera sie pole z menu
    w srodku opcje
        1.nowe
            trzeba podac tytul np platformy i tworzy sie
        2.stare
            biblioteka z haslami dodanymi juz do tej pory
        3.zmien haslo
            tworzy nowe haslo dla wybranego katalogu
3.generator hasel o dlugosci 15
4.kopiowanie sie hasel do schowka
5.moze jakis rodzaj zabezpieczen
'''
from tkinter import Button, Label, Tk
from login import Login
from register import Register


class StartWindow:
    def __init__(self):
        #okno startowe calego programu
        self.app = Tk()
        self.app.title("Login with Python")
        self.app.geometry("300x200")
        self.label = Label(self.app, text="Welcome to App")
        self.label.place(x=95, y=40)
        self.login = Button(self.app, text="Login",pady=5,padx=30, command = login)
        self.login.place(x=100, y=100)
        self.register = Button(self.app, text="Register",pady=5, padx=20,command=register)
        self.register.place(x=100, y=150)

    def run(self):
        self.app.mainloop()

#uruchamianie logowania sie
def login():
    loginTk = Login()
    loginTk.run()
#uruchamianie rejestracji
def register():
    registerTk = Register()
    registerTk.run()

#odpalanie sie programu
app = StartWindow()
app.run()
