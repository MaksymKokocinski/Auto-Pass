import sys
from tkinter import Button, Label, Tk, Listbox
from tkinter import messagebox
"""
Stworzyc generator i sprawic zeby hasla sie zapisywale, ogarnac co nie dziala i baze danych
"""

class MainWindow():
    def __init__(self):
        #wyglad glownego okna
        self.mw = Tk()
        self.mw.title("Main window")
        self.mw.geometry("400x400")
        self.label = Label(self.mw, text="Welcome to main menu")
        self.label.place(x=125, y=20)

        self.login = Button(self.mw, text="NewPassword",pady=5,padx=30, command = newpass)
        self.login.place(x=50, y=90)
        self.login = Button(self.mw, text="Show/hide",pady=5,padx=30, command = showhide)
        self.login.place(x=225, y=90)
        self.register = Button(self.mw, text="Logout",pady=5, padx=30,command=logout)
        self.register.place(x=225, y=40)
        self.register = Button(self.mw, text="info",pady=5, padx=30,command=info)
        self.register.place(x=50, y=40)
        #listbox dla nazw folderow
        self.listbox = Listbox(self.mw)
        self.listbox.insert(1, "Test1")
        self.listbox.insert(2, "Test2")
        self.listbox.insert(3, "Test3")
        self.listbox.insert(4, "Test4")
        self.listbox.insert(5, "Test5")
        self.listbox.insert(6, "Test6")
        self.listbox.pack()
        self.listbox.place(x=50, y=140)
        #listbox dla hasel
        self.listbox2 = Listbox(self.mw)
        self.listbox2.insert(1, "Test1")
        self.listbox2.insert(2, "Test2")
        self.listbox2.insert(3, "Test3")
        self.listbox2.insert(4, "Test4")
        self.listbox2.insert(5, "Test5")
        self.listbox2.insert(6, "Test6")
        self.listbox2.pack()
        self.listbox2.place(x=225, y=140)


    #odpalanie okienka
    def run(self):
        self.mw.mainloop()
#funkcja w ktorej bd generowane nowe haslo
def newpass():
    messagebox.showinfo("NewPassword","New password will be generated here")

def info():
    messagebox.showinfo("Info","Info")    
def showhide():
    messagebox.showinfo("showhide","showhide") 
#zamykanie programu
def logout():
    messagebox.showinfo("Logging out","Logged out")
    sys.exit()



    


#testowe otwieranie glownego okna
"""mw = MainWindow()
mw.run()
"""