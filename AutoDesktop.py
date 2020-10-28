#----Auto Desktop-------
'''
1 Otwieranie folderow z ktorych chcemy sortowac rzeczy
2 Przenoszenie ich do danego folderu
3 Analizowanie folderow po tytule i rozszerzeniu
 Grupowanie je po nazwie a foldery przerzuca jako foldery
4 napisanie ze koniec i elo
5 automatycznie to sie ma odpalac a moze nie?
'''
#przeniesienie wszystkich rzeczy do wideo i tam sortowanie ich

#dodanie opcji wybrania lokacji pliku z ktorego chcesz
#sortowac i ich ilosci
#dodanie opcji wybrania dokad ma byc zapisane
#jednorazowe
import os
import shutil

Pulpit='C:/Users/Maksym Kokocinski/Desktop'
Pobrane='C:/Users/Maksym Kokocinski/Downloads'
Wideo='C:/Users/Maksym Kokocinski/Videos'

def sortowanie():
    sciezka=Wideo
    lista = os.listdir(sciezka)
    #print(lista)
    for plik in lista:
        nazwa, rozsz =os.path.splitext(plik)

        rozsz = rozsz[1:]

        if rozsz == '':
            continue

        if os.path.exists(sciezka+'/'+rozsz):
            shutil.move(sciezka+'/'+plik,sciezka+'/'+'/'+rozsz+'/'+plik)
    
        else:
            os.makedirs(sciezka+'/'+rozsz)
            shutil.move(sciezka+'/'+plik,sciezka+'/'+'/'+rozsz+'/'+plik)
    print("Posortowane")

def przeniesieniePulpit():
    sciezka1=Pulpit
    lista1=os.listdir(sciezka1)
    for plik1 in lista1:
        shutil.move(os.path.join(Pulpit,plik1),Wideo)
    print("Przeniesione Pulpit")

def przeniesieniePobrane():
    sciezka2=Pobrane
    lista2=os.listdir(sciezka2)
    for plik2 in lista2:
        shutil.move(os.path.join(Pobrane,plik2),Wideo)
    print("Przeniesione Pobrane")

def usunini():
    try:
        shutil.rmtree("C:/Users/Maksym Kokocinski/Videos/ini")
    except:
        print("Nie ma ini")


def main():
    przeniesieniePulpit()
    sortowanie()
    usunini()
    przeniesieniePobrane()
    sortowanie()
    usunini()

main()