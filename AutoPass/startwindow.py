#dodac guzik z info i stworzyc nowa klase z oknem informacji i guzik wyjscie
from tkinter import Button, Label, Tk, messagebox
from login import Login
from register import Register
from database import Database


class StartWindow:
    def __init__(self):
        #okno startowe calego programu
        self.app = Tk()
        self.app.title("Login with Python")
        self.app.geometry("300x200")
        self.label = Label(self.app, text="Welcome to Password Manager")
        self.label.place(x=65, y=55)
        self.login = Button(self.app, text="Login",pady=5,padx=30,command = self.logandquit)
        self.login.place(x=100, y=100)
        self.register = Button(self.app, text="Register",pady=5, padx=25,command=self.regandquit)
        self.register.place(x=100, y=150)
        self.info = Button(self.app, text="Info",pady=5,padx=20,command = self.info)
        self.info.place(x =220, y=10)

        whatoperation()
    #odpalanie okna
    def run(self):
        self.app.mainloop()
    #zamykanie okna 
    def quit(self):
        self.app.destroy() 
    #okno z informacją co i jak
    def info(self):
        self.message = "Hello, if it is your first use of the program you need to create an account using the button register!, Otherwise, you need to login, because there is a limit of 1 account per folder."
        messagebox.showinfo('Info',self.message3)

    #zamykanie okna po wyskoczeniu okienka do logowania
    def logandquit(self):
        if canlogin == True:
            self.quit()
            login()
        else:
            messagebox.showinfo("Error", "You need to register first") 
    #zamykanie okna po wyskoczeniu okienka do logowania
    def regandquit(self):
        if canlogin == False:
            self.quit()
            register()
        else:
            messagebox.showinfo("Error", "You can't register, there is an account already") 

#funkcja ktora sprawdza, czy jest uzytkownik i mozna sie zalogowac czy 
def whatoperation():
    global canlogin
    db = Database()
    if db.userMaker() == 1:
        canlogin = True
    else:
        canlogin = False

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
