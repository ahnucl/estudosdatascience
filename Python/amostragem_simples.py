"""
    Aula amostragem I com Python
"""
import pandas as pd 
# biblioteca usada em ciência de dados para trabalhar com  dataframes e bases de dados
import numpy as np
# numpy tem funções estatísticas

base = pd.read_csv('iris.csv') #função do panda para ler csv

base.shape

np.random.seed(2345) # semelhante ao do R também - fixa um "seed" para permitir a repetibilidade de experimentos
amostra = np.random.choice(a = [0,1], size = 150, replace = True, p = [0.5,0.5])
# usar o array gerado com zeros e uns para selecionar os "uns" do meu conjunto de dados como amostra

len(amostra)

len(amostra[amostra==1]) # parece o filtro do R
len(amostra[amostra==0])
