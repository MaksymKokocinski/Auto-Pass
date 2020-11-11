import bcrypt
from tkinter import Button, Label, Tk, Entry, StringVar, FLAT, messagebox
from database import Database
from mainwindow import MainWindow

db = Database()
db.createTable()
#dodac info gdzies i guzik cofnij
class Login:
    def __init__(self):

        #Wyglad okienka logowania sie
        self.loginWindow = Tk()
        self.loginWindow.title("Login with Python")
        self.loginWindow.geometry("300x250")
        self.label = Label(self.loginWindow, text = "Login")
        self.label.place(x=95, y=40)

        # zmienne narazie potrzebne
        self.usernameS = StringVar()
        self.passwordS = StringVar()
        self.usernameE = Entry (
            self.loginWindow, relief=FLAT, textvariable=self.usernameS)
        self.usernameE.place(x=70, y=80)
        self.passwordE = Entry (
            self.loginWindow, show="*", relief=FLAT, textvariable=self.passwordS)
        self.passwordE.place(x=70, y=120)

        #faktyczne zmienne
        self.username = self.usernameS.get()
        self.password = self.passwordS.get()
        self.submit = Button(self.loginWindow, text="Submit",pady = 5, padx =20, command=self.validate)
        self.submit.place(x=100, y=150)
    
    #uwierzytelnianie
    def validate(self):
        data=(self.username,)
        inputData = (self.username,self.password,)
        try:
            if (db.validateData(data, inputData)):
                messagebox.showinfo ("Successful", "Login was Successful")
                self.quit()
                mainwindow()
                
            else:
                messagebox.showinfo ("Unsuccessful", "Login was Unsuccessful")
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

        
     