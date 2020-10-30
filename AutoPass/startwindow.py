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

#dodac guzik z info i stworzyc nowa klase z oknem informacji i guzik wyjscie
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
        self.login = Button(self.app, text="Login",pady=5,padx=30,command = self.logandquit)
        self.login.place(x=100, y=100)
        self.register = Button(self.app, text="Register",pady=5, padx=20,command=self.regandquit)
        self.register.place(x=100, y=150)
    #odpalanie okna
    def run(self):
        self.app.mainloop()
    #zamykanie okna 
    def quit(self):
        self.app.destroy() 
    #zamykanie okna po wyskoczeniu okienka do logowania
    def logandquit(self):
        self.quit()
        login()
    #zamykanie okna po wyskoczeniu okienka do logowania
    def regandquit(self):
        self.quit()
        register()
        

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