# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:28:51 2020

@author: Leo
"""

"""
import statistics as sta


"""

"""
OU
"""

#from statistics import mean, median
from statistics import * # mostra um warning

z = [10,20,20,40]

#x = sta.mean(z)
#y = sta.median(z)

x = mean(z)
y = median(z)
print(x)
print(y)


"""
Funções
"""
from numpy import *

aula = 2;
if aula == 1:
    def imprimir(n = 10):
        #print("valor = " + str(n))
        print("valor = ",n)
        
    def retornar_algo(nome):
        return "Seu nome é " + nome
    
    print(retornar_algo("João"))
    
    imprimir()
    
    
    def intervalo(inic = 1, fim = 10):
        for inic in range(1,fim+1):
            print(inic)
      
            
    intervalo(12,15)
    intervalo()
else:
   
    a = random.random((8,8))
    #print(type(a))
    print(a)
