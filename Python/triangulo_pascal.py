# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:43:08 2020

@author: Leonardo.Cunha
"""

# Cálculo do triângulo de Pascal
import math as ma

n = 0
fact_i = 0
resultado = 0
fact_n= 0

for i in range(10):
    fact_i = ma.factorial(i)
    for n in range(i+1):
        fact_n = ma.factorial(n)
        resultado = fact_i/(fact_n * ma.factorial(i-n))  
        print('(i,n)=('+str(i)+','+str(n)+') = '+str(resultado))
        
    
    
    
    
