import sys
import random
import pyperclip
from tkinter import Button, Label, Tk, Listbox, messagebox, ttk, Frame, Scrollbar,Entry,END,NO,RIGHT,LEFT,W,Y,X,BOTTOM,TOP

mw = Tk()
mw.title('Main Window')
mw.geometry("500x500")
# Create Treeview Frame
tree_frame = Frame(mw)
tree_frame.place(x=200, y=120)
#Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill = Y)
#Create Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand = tree_scroll.set)
# Pack to the screen
my_tree.pack()
#Configure the scrollbar
tree_scroll.config(command=my_tree.yview)
#Define Our Columns
my_tree['columns'] = ("Platform", "Password")
# Formate Our Columns
my_tree.column("#0", width = 0, stretch = NO)
my_tree.column("Platform", anchor = W, width = 120)
my_tree.column("Password", anchor = W, width = 120)
# Create  Headings 
my_tree.heading("#0",text = "", anchor = W)
my_tree.heading("Platform", text = "Platform",anchor = W)
my_tree.heading("Password", text="Password", anchor = W)
# Add Data
data =[
    ["Youtube","Peperroni"],
    ["Twitch","Julkakulka1"],
    ["Facebook","Potato"],
    ["Microsoft","Lolik"],
    ["Skype","Max1"]
]
global count
count = 0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]))
    count += 1

add_frame =Frame (mw)
add_frame.place(x=200, y=60)

#Labels
nl = Label(add_frame, text = "Platform")
nl.grid(row = 0, column = 0)
tl = Label(add_frame, text = "Password")
tl.grid(row=0, column = 2)
#Entry boxes
platform_box = Entry(add_frame)
platform_box.grid(row=1, column = 0)
password_box = Entry(add_frame)
password_box.grid(row=1, column = 2)
#Add Record
def add_record():
    global count
    my_tree.insert(parent='', index='end', iid=count, text="", values=(platform_box.get(),password_box.get()))
    count += 1
    platform_box.delete(0, END)
    password_box.delete(0, END)
# Remove all records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

def select_record():
    #clear entry boxes
    platform_box.delete(0, END)
    password_box.delete(0, END)
    #Grab record number
    selected = my_tree.focus()
    #Grab record values
    values = my_tree.item(selected, 'values')
    #output to entry boxes
    platform_box.insert(0, values[0])
    password_box.insert(0, values[1])

def update_record():
    #Grab record number
    selected = my_tree.focus()
    #Save new data
    my_tree.item(selected, text = "", values = (platform_box.get(),password_box.get()))
    #clear after
    platform_box.delete(0, END)
    password_box.delete(0, END)

def generate():
            randompass()
            pyperclip.copy(generatedpassword)
            pyperclip.paste()

def info():
    messagebox.showinfo("Info","Info")

def logout():
    messagebox.showinfo("Logging out","Logged out")
    sys.exit()

label = Label(mw, text = "Welcome, here you can manage your passwords, for more info click ->")        
label.place(x=40, y=30)
#Buttons
info = Button(mw, text="Info",pady=5,padx=12,command=info)
info.place(x=420, y=20)
add_record = Button(mw, text="Add One Password",pady=5,padx=22,command=add_record)
add_record.place(x=40, y=80)
generate = Button(mw, text="Generate Password",pady=5,padx=22,command=generate)
generate.place(x=40, y=120)
select_record = Button(mw, text="Select One Password",pady=5,padx=16,command=select_record)
select_record.place(x=40, y=160)
update_record = Button(mw, text="Save One Password",pady=5,padx=20,command=update_record)
update_record.place(x=40, y=200)
remove_one = Button(mw, text="Remove One Selected",pady=5,padx=14,command=remove_one)
remove_one.place(x=40, y=240)
remove_many = Button(mw, text="Remove Many Selected",pady=5,padx=10,command=remove_many)
remove_many.place(x=40, y=280)
remove_all = Button(mw, text="Remove All Passwords",pady=5,padx=12,command=remove_all)
remove_all.place(x=40, y=320)

logout = Button(mw, text="Log out",pady=5,padx=10,command=logout)
logout.place(x=40, y=450)

def randompass():
        maxlen = 10

        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

        smallchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 
        
        bigchar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O',
                'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 
        
        symb = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<','&','#'] 
        #laczenie wszystkich znakow
        allchar= digits + smallchar + bigchar + symb
        """randomdigit = random.choice(digits)
        randomsmallchar = random.choice(smallchar)
        randombigchar = random.choice(bigchar)
        randomsymbol = random.choice(symb)"""
        #robienie sie hasla
        global generatedpassword
        generatedpassword = ""
        for _ in range(maxlen):
            generatedpassword = generatedpassword + random.choice(allchar)
        infopassword = ("Your new password:\n"+generatedpassword+"\nCopied to clipboard!")
        messagebox.showinfo("Generated Password",infopassword)


mw.mainloop()






