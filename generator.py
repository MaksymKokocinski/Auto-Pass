import random
import bcrypt
from tkinter import Button, Label, Tk, Entry, StringVar, FLAT, messagebox
from database import Database
# zrobic ze imput musi byc do kazdego hasla z tytulem do czego ono jest

class NewPass:
    def __init__(self):
        # wyglad okienka rejestrowania sie
        self.newpassWindow = Tk()
        self.newpassWindow.title("Generate new password with Python")
        self.newpassWindow.geometry("300x250")
        self.label = Label(self.newpassWindow, text = "NewPassword")
        self.label.place(x=95, y=40)

        # zmienne puste potrzebne
        global usernameS
        global passwordS
        usernameS = StringVar()
        passwordS = StringVar()
        #pola do pisania i guzik commita
        usernameE = Entry ( self.newpassWindow, relief=FLAT, textvariable= usernameS)
        usernameE.place(x=70, y=80)
        passwordE = Entry ( self.newpassWindow, show="*", relief=FLAT, textvariable= passwordS)
        passwordE.place(x=70, y=120)
        self.submit = Button(self.newpassWindow,text ="Submit", pady =5, padx = 20, command=self.commit)
        self.submit.place(x=100, y=150)
        self.submit = Button(self.newpassWindow,text ="Generate", pady =5, padx = 5, command=self.commit)
        self.submit.place(x=210, y=110)
        #odpalanie sie rejestrowania

    def commit(self):
        #zbieranie zmiennych po nacisnieciu guzika i wysylanie ich do bazy danych
        global username
        global password
        username = usernameS.get()
        password = passwordS.get()

    def run(self):
        self.newpassWindow.mainloop()
    #zamykanie okna rejestracji
    def quit(self):
        self.newpassWindow.destroy()    
           
class RandomPass():
    def __init__(self):
        self.maxlen = 16

        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

        self.smallchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 
        
        self.bigchar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O',
                'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 
        
        self.symb = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<','&','#'] 
        #laczenie wszystkich znakow
        self.allchar= self.digits + self.smallchar + self.bigchar + self.symb

        #losowy znak bd z kazdej z tabeli
        #nie jest chyba potrzebny bo mozna wygenerowac nastepne
        """randomdigit = random.choice(digits)
        randomsmallchar = random.choice(smallchar)
        randombigchar = random.choice(bigchar)
        randomsymbol = random.choice(symb)"""
        
        #robienie sie hasla
        self.temppass = ""
        for letter in range(self.maxlen):
            self.temppass = self.temppass + random.choice(self.allchar)
        print(self.temppass)

RandomPass()
mw = NewPass()
mw.run()