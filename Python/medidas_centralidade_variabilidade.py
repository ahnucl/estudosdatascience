# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:28:25 2020

@author: Leonardo.Cunha
"""

# medidas de centralidade
import numpy as np
from scipy import stats # acho que essa notação é para não importar o pacote inteiro
"""
    Funções de estatística ^^^
"""

jogadores = [40000,  18000,  12000, 250000 , 30000 ,140000 ,300000 , 40000,  800000
]

# media
np.mean(jogadores)

# mediana
np.median(jogadores)

# quartis
quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1]) # passado um array com os quartis que se deseja calcular

# desvio padrão
np.std(jogadores)
"""
    Diferença de cálculo do desvio padrão entre o python e o R
    no R o cálculo é feito usando n-1 (amostra)
    no python, por padrão, é usado n -> para usar n-1 passar o parâmetro ddof=1
    lembrando, selecionar função e pressionar ctrl+i para exibir a ajuda
    Na ajuda existe explicação dos parâmetros
"""

np.std(jogadores, ddof = 1)

stats.describe(jogadores)

# cálculo nativo da Moda
stats.mode(jogadores)