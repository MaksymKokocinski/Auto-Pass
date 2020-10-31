import random
#import array

#zastanowic sie czy nie zlosowac hasla jeszce raz albo jakis element losowosci w nim wprowadzic
# zrobic ze imput musi byc do kazdego hasla z tytulem do czego ono jest
class RandomPass():
    def __init__(self):
        maxlen = 12

        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

        smallchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 
        
        bigchar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O',
                'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 
        
        symb = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<','&','#'] 
        #laczenie wszystkich znakow
        allchar= digits + smallchar + bigchar + symb

        #losowy znak bd z kazdej z tabeli
        randomdigit = random.choice(digits)
        randomsmallchar = random.choice(smallchar)
        randombigchar = random.choice(bigchar)
        randomsymbol = random.choice(symb)

        #robienie sie hasla
        temppass = ""
        for letter in range(maxlen-4):
            temppass = temppass + random.choice(allchar)
        temppass = temppass + randomdigit + randomsmallchar + randombigchar + randomsymbol
        print(temppass)

RandomPass()