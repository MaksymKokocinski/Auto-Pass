import sqlite3
import bcrypt

class Database:
    def __init__(self):
        #lokalizacja bazy danych i kursor do bazy danych
        try:
            self.conn = sqlite3.connect("AutomationProjects/AutoPass/AutoPassDatabase.db")
            #print("Successfully Opened Database")
            self.curr = self.conn.cursor()
        except:
            print("Failed 1")
    
    def createTable(self):
        #tworzenie tabeli z loginami w bazie danych
        create_table = """
        CREATE TABLE IF NOT EXISTS accounts(
        id Integer PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL);
        """
        self.curr.execute(create_table)
        self.conn.commit()

    def insertData(self,data):
        #wprowadzanie danych do bazy danych
        insert_data= """
        INSERT INTO accounts(username, password) VALUES(?, ?);
        """
        self.curr.execute(insert_data, data)
        self.conn.commit()
        #self.userMaker()

    def searchData(self, data):
        #sprawdzanie czy taki login jest juz w bazie danych
        search_data ="""
        SELECT * FROM accounts WHERE username = (?);
        """
        self.curr.execute(search_data, data)
        rows = self.curr.fetchall()
        self.userMaker()
        if rows == [] and usernumber == 0:
            return 1
        else:
            return 0
    def validateData(self, data, inputData):
        #uwierzytelnianie danych przed zalogowaniem do main window

        validate_data = """
        SELECT * FROM accounts WHERE username = (?);
        """
        #print("dataDB:",data)
        #print("input dataDB:",inputData)
        self.curr.execute(validate_data, data)
        row = self.curr.fetchall()
        #print("row",row)
        self.userMaker()
        if row[0][1] == inputData[0]:
            return row[0][2] == bcrypt.hashpw(inputData[1].encode(), row[0][2])#tutaj encoduje
                       
    def userMaker(self):
        self.curr.execute("SELECT count(id) FROM accounts")
        datanumber = self.curr.fetchall()
        #print("datanumber:",datanumber[0])
        global usernumber
        if str(datanumber[0]) =="(0,)":
            usernumber = 0
        else:
            usernumber = 1    
##################################################################################################

class Database2:
    def __init__(self):
        #lokalizacja bazy danych i kursor do bazy danych
        try:
            self.conn = sqlite3.connect("AutomationProjects/AutoPass/AutoPassDatabase.db")
            #print("Successfully Opened Database2")
            self.curr = self.conn.cursor()
        except:
            print("Failed 2")
    
    def createTable(self):
        #tworzenie tabeli z loginami w bazie danych
        create_table = """
        CREATE TABLE IF NOT EXISTS userdata(
        id Integer PRIMARY KEY AUTOINCREMENT, platform TEXT NOT NULL, password TEXT NOT NULL);
        """
        self.curr.execute(create_table)
        self.conn.commit()

    def insertData(self,data):
        #wprowadzanie danych do bazy danych
        insert_data= """
        INSERT INTO userdata(platform, password) VALUES(?, ?);
        """
        self.curr.execute(insert_data, data)
        self.conn.commit()
        #self.userMaker()

    def searchData(self, data):
        #sprawdzanie czy taki login jest juz w bazie danych
        search_data ="""
        SELECT * FROM userdata WHERE platform = (?);
        """
        self.curr.execute(search_data, data)
        rows = self.curr.fetchall()
        if rows == []:
            return 1
        else:
            return 0
    
    def readData(self):
        read_data = """
        SELECT platform, password FROM userdata;
        """
        self.curr.execute(read_data)
        global count
        count = 0
        global inputData
        inputData = []
        for row in self.curr.fetchall():
            inputData += row[0],row[1]
        return inputData

    def updateData(self,data):
        #wprowadzanie danych do bazy danych
        update_data= """
        UPDATE userdata SET platform = ?, password = ? WHERE platform = ?;
        """
        self.curr.execute(update_data, data)
        self.conn.commit()

    def deleteData(self,data):
        delete_data = """
        DELETE FROM userdata WHERE platform = ?;
        """
        self.curr.execute(delete_data, data)
        self.conn.commit()
    
    def deleteAcc(self):
        deleteUser = """
        DELETE FROM accounts
        """
        self.curr.execute(deleteUser)
        self.conn.commit()
    def DeletePass(self):
        deletePasswords = """
        DELETE FROM userdata
        """
        self.curr.execute(deletePasswords)
        self.conn.commit()


        