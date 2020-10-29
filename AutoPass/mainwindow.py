
import sys
from tkinter import Button, Label, Tk, Listbox
from tkinter import messagebox


class MainWindow():
    def __init__(self):
        self.mw = Tk()
        self.mw.title("Main window")
        self.mw.geometry("300x400")
        self.label = Label(self.mw, text="Welcome to main menu")
        self.label.place(x=100, y=40)

        self.login = Button(self.mw, text="NewPassword",pady=5,padx=30, command = newpass)
        self.login.place(x=100, y=60)

        self.listbox = Listbox(self.mw)
        self.listbox.insert(1, "Test1")
        self.listbox.insert(2, "Test2")
        self.listbox.insert(3, "Test3")
        self.listbox.insert(4, "Test4")
        self.listbox.insert(5, "Test5")
        self.listbox.insert(6, "Test6")
        self.listbox.pack()
        self.listbox.place(x=100, y=100)

        
        self.register = Button(self.mw, text="Logout",pady=5, padx=30,command=logout)
        self.register.place(x=100, y=300)

    def run(self):
        self.mw.mainloop()
    
def newpass():
    messagebox.showinfo("NewPassword","New password will be generated here")

def logout():
    messagebox.showinfo("Logging out","Logged out")
    sys.exit()



    


#testowe otwieranie glownego okna
mw = MainWindow()
mw.run()
