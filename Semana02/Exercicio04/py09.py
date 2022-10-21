
#Maneiras diferentes que se pode importar um conteudo:
#import py09_module
#import py09_module as md
#from py09_module import find_index as fi, teste as tst
#from py09_path.py09_module import * 
#------------------------------------------------
import sys #Importing python sytem module

#Se o modulo estiver em outra pasta, podemos tambem fazer:
#sys.path.append('/home/salomao/Desktop/SEII/SEII-GuilhermeSalomaoAgostinii/Semana02/Exercicio04/py09_path')
#from py09_module import * 

#----------------------------------------------
#Outra forma:
from py09_path.py09_module import *
#----------------------------------------------


courses = ['History', 'Math', 'Phisics', 'Art']
#index = py09_module.find_index(courses,'Math')
#index = md.find_index(courses,'Math')
index = find_index(courses,'Math')
#index = fi(courses,'Math')

print (index)
print (teste)
#print (tst)

print(sys.path) #Imprime na tela Python Path



import random
random_course = random.choice(courses) #Randomiza um elemento de courses
print(random_course)


import math
print(math.radians(90)) #Radianos de 90 graus

import datetime
print(datetime.date.today()) #Passa o dia de hoje

import os
print(os.listdir()) #Lista todos os arquivos e diretorios da pasta onde o arquivo se encontra

#import antigravity