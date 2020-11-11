import random
#import array

# zrobic ze imput musi byc do kazdego hasla z tytulem do czego ono jest
class RandomPass():
    def __init__(self):
        self.maxlen = 12

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