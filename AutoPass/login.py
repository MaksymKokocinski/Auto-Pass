import bcrypt
from tkinter import Button, Label, Tk, Entry, StringVar, FLAT, messagebox
from database import Database
from mainwindow import MainWindow

class Login:
    def __init__(self):

        #Wyglad okienka logowania sie
        self.loginWindow = Tk()
        self.loginWindow.title("Login with Python")
        self.loginWindow.geometry("300x250")
        self.label = Label(self.loginWindow, text = "Enter login and password for your account")
        self.label.place(x=30, y=40)

        # zmienne puste potrzebne
        global usernameS
        global passwordS
        usernameS = StringVar()
        passwordS = StringVar()
        #pola do pisania i guzik do commita
        usernameE = Entry (self.loginWindow, relief=FLAT, textvariable=usernameS)
        usernameE.place(x=85, y=80)
        passwordE = Entry (self.loginWindow, show="*", relief=FLAT, textvariable=passwordS)
        passwordE.place(x=85, y=120)
        self.submit = Button(self.loginWindow, text="Submit",pady = 5, padx =20, command=self.commit)
        self.submit.place(x=100, y=150)

    def commit(self):
        #zbieranie zmiennych po nacisnieciu guzika i wysylanie ich do bazy danych
        global username
        global password
        username = usernameS.get()
        password = passwordS.get()
        #print('pass',password)
        self.validate()

    #uwierzytelnianie
    def validate(self):
        db = Database()
        data=(username,)
        inputData = (username,password,)
        try:
            if (db.validateData(data, inputData)):
                messagebox.showinfo ("Successful", "Login was Successful")
                self.quit()
                mainwindow()    
            else:
                messagebox.showinfo ("Unsuccessful", "Login was Unsuccessful, wrong password")
        except IndexError:
            messagebox.showinfo ("Unsuccessful", "Login was Unsuccessful")

    #uruchamianie okienka loginu
    def run(self):
        self.loginWindow.mainloop()
    #zamykanie okienka loginu
    def quit(self):
        self.loginWindow.destroy() 
        
#otwieranie nastepnego okna
def mainwindow():
    mainwindowTk = MainWindow()
    mainwindowTk.run()
  
     