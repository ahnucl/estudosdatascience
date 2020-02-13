
"""
Amostragem sistemática, sem bibliotecas - feita na mão!

@author: Leonardo.Cunha
"""

import numpy as np
import pandas as pd
from math import ceil

populacao = 150
amostra = 15
k = ceil(populacao/amostra)

#Sorteio de um número entre 1 e k
r = np.random.randint(low = 1, high = k + 1, size = 1)

acumulador = r[0] # r está em formato de vetor
sorteados = [] # lista vazia

for i in range(amostra):
    sorteados.append(acumulador)
    acumulador += k
    

base = pd.read_csv('iris.csv')
base_final = base.loc[sorteados] # notação de splice, semelhante aos filtros

