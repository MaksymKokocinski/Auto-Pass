import sqlite3
import bcrypt

class Database:
    def __init__(self):
        #lokalizacja bazy danych i kursor do bazy danych
        try:
            self.conn = sqlite3.connect("ProPython/AutomationProjects/AutoPass/AutoPassDatabase.db")
            #print("Successfully Opened Database")
            self.curr = self.conn.cursor()
        except:
            print("Failed")
    
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
        self.userMaker()

    def searchData(self, data):
        #sprawdzanie czy taki login jest juz w bazie danych
        search_data ="""
        SELECT * FROM accounts WHERE username = (?);
        """
        self.curr.execute(search_data, data)

        rows = self.curr.fetchall()

        if rows == []:
            return 1
        else:
            return 0
    def validateData(self, data, inputData):
        #uwierzytelnianie danych przed zalogowaniem do main window

        validate_data = """
        SELECT * FROM accounts WHERE username = (?);
        """
        self.curr.execute(validate_data, data)
        row = self.curr.fetchall()
        self.userMaker()
        
        if row[0][1] == inputData[0]:
            return row[0][2] == bcrypt.hashpw(inputData[1].encode(), row[0][2])

        

    """Wszystko od tego momentu jest do tabeli wyświetlanych w głownym menu """




    def createTable2(self):
            #tworzenie tabeli z pllatformami i ich hasłami w bazie danych
            create_table2 = """
            CREATE TABLE IF NOT EXISTS id"""+usernumber+"""(
            id Integer PRIMARY KEY AUTOINCREMENT, platform TEXT, ppassword TEXT);
            """
            self.curr.execute(create_table2)
            self.conn.commit()

    def insertData2(self,data):
        #wprowadzanie danych do bazy danych
        insert_data2= """
        INSERT INTO id"""+usernumber+"""(platform, ppassword) VALUES(?, ?);
        """
        self.curr.execute(insert_data2, data)
        self.conn.commit()
        self.userMaker()

    def searchData2(self, data):
        #sprawdzanie czy taki login jest juz w bazie danych
        search_data2 ="""
        SELECT * FROM id"""+usernumber+""" WHERE platform = (?);
        """
        self.curr.execute(search_data2, data)

        rows = self.curr.fetchall()

        if rows == []:
            return 1
        else:
            return 0
    def validateData2(self, data, inputData):
        #uwierzytelnianie danych przed zalogowaniem do main window

        validate_data2 = """
        SELECT * FROM id"""+usernumber+""" WHERE platform = (?);
        """
        self.curr.execute(validate_data2, data)
        row = self.curr.fetchall()

        if row[0][1] == inputData[0]:
            return row[0][2] == bcrypt.hashpw(inputData[1].encode(), row[0][2])
           
    def userMaker(self):
        self.curr.execute("SELECT count(id) FROM accounts")
        datanumber = self.curr.fetchall()
        print(datanumber)

        for temp1 in range(100):
            temp1 = temp1 + 1
            temp2 = str(temp1)
            temp2 = '('+temp2 + ','+')'
            if temp2 == str(datanumber[0]):
                print("mamy to",temp1)
                global usernumber
                usernumber =str(temp1)
        self.createTable2()
                    


        