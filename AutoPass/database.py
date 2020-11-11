import sqlite3
import bcrypt

class Database:
    def __init__(self):
        #lokalizacja bazy danych i cursor do bazy danych
        try:
            self.conn = sqlite3.connect("ProPython/AutomationProjects/AutoPass/AutoPassDatabase.db")
            print("Successfully Opened Database")
            self.curr = self.conn.cursor()
        except:
            print("Failed")
    
    def createTable(self):
        #tworzenie tabeli z loginami w bazie danych
        create_table = """
        CREATE TABLE IF NOT EXISTS cred(
        id Integer PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL);
        """
        self.curr.execute(create_table)
        self.conn.commit()

    def insertData(self,data):
        #wprowadzanie danych do bazy danych

        insert_data= """
        INSERT INTO cred(username, password) VALUES(?, ?);
        """
        self.curr.execute(insert_data, data)
        self.conn.commit()

    def searchData(self, data):
        #sprawdzanie czy taki login jest juz w bazie danych
        search_data ="""
        SELECT * FROM cred WHERE username = (?);
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
        SELECT * FROM cred WHERE username = (?);
        """
        self.curr.execute(validate_data, data)
        row = self.curr.fetchall()

        if row[0][1] == inputData[0]:
            return row[0][2] == bcrypt.hashpw(inputData[1].encode(), row[0][2])
        