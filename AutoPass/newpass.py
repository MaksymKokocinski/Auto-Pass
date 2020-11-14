import random
import bcrypt
from tkinter import Button, Label, Tk, Entry, StringVar, FLAT, messagebox
from database import Database
db = Database()
db.createTable()

class NewPass:
    def __init__(self):
        # wyglad okienka rejestrowania sie
        self.newpassWindow = Tk()
        self.newpassWindow.title("Generate new password with Python")
        self.newpassWindow.geometry("300x250")
        self.label = Label(self.newpassWindow, text = "NewPassword")
        self.label.place(x=95, y=20)

        # zmienne puste potrzebne
        global platS
        global passS
        platS = StringVar()
        passS = StringVar()
        #pola do pisania i napisy
        self.label = Label(self.newpassWindow, text="Platforrm :")
        self.label.place(x=70, y=60)
        usernameE = Entry ( self.newpassWindow, relief=FLAT, textvariable= platS)
        usernameE.place(x=70, y=80)
        self.label = Label(self.newpassWindow, text="Password :")
        self.label.place(x=70, y=100)
        passwordE = Entry ( self.newpassWindow, relief=FLAT, textvariable= passS)
        passwordE.place(x=70, y=120)
        #guziki
        self.submit = Button(self.newpassWindow,text ="Submit", pady =5, padx = 20, command=self.commit)
        self.submit.place(x=100, y=150)
        self.submit2 = Button(self.newpassWindow,text ="Generate", pady =5, padx = 5, command=self.generate)
        self.submit2.place(x=210, y=110)
    

    #funkcja do przechowywania hasla w schowku przez 500 sekund
    def generate(self):
        self.randompass()
        self.temp = Tk()
        self.temp.withdraw()
        self.temp.clipboard_clear()
        self.temp.clipboard_append(generatedpassword)
        self.temp.update()
        self.temp.after(500,self.temp.destroy)
        self.temp.mainloop()

    def commit(self):
        #zbieranie zmiennych po nacisnieciu guzika i wysylanie ich do bazy danych
        global platform
        global password
        #print("1",platS.get(),passS.get())
        platform = platS.get()
        password = passS.get()
        print("pass, plat:",password,platform)#nie dziala jak sie odpala z poza tej strony
        self.add()

    def add(self):
        data = (platform,)
        result = db.searchData2(data)
        if result != 0:
            data = (platform,password)
            db.insertData2(data)
            messagebox.showinfo("Successful", "Platform Was Added")
            self.quit()
              
        else:
            messagebox.showwarning("Warning", "Platform already Exists, try again")

    #odpalanie
    def run(self):
        self.newpassWindow.mainloop()

    #zamykanie okna rejestracji
    def quit(self):
        self.newpassWindow.destroy()    

             

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

        #losowy znak bd z kazdej z tabeli
        #nie jest chyba potrzebny bo mozna wygenerowac nastepne
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



"""
mw = NewPass()
mw.run()"""