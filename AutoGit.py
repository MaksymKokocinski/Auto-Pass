'''
1. Wchodzenie do danego folderu z projektami
    analizowanie co gdzie i jak i wrzucanie do listy
    przechodzenie z folderu do folderu
2. zapisywanie plikow i ich zawartosci
3. wysylanie do gita
    tworzenie repozytorium jak nie ma
    tworzenie projektu jak nie ma 
4. Pytanie czy chcesz wyslac zaktualizowane rzeczy
5. dodawanie wyjatkow
'''
import os
import shutil
import subprocess as cmd
import base64
from github import Github
from github import InputGitTreeElement


file_list=['C:/Users/Maksym Kokocinski/Documents/VSCode/Learning/ProPython/ProAlg.py']
repo =['https://github.com/MaksymKokocinski?tab=repositories']

def otwieranie():
    sciezka=file_list
    lista = os.listdir(sciezka)
    print(lista)
    #for plik in lista:

from git import Repo

repo_dir = 'mathematics'
repo = Repo(repo_dir)

commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()