"""
    amostragem estratificada

@author: Leonardo.Cunha
"""

import pandas as pd
from sklearn.model_selection import train_test_split # atenção nessa linha!

iris = pd.read_csv('iris.csv')

iris["class"].value_counts() # contagem da coluna 

# Gerar a amostragem com 50% dos dados

x, _, y, _ = train_test_split(iris.iloc[:, 0:4],  # python não tras o upperbound
                              iris.iloc[:,4], 
                              test_size = 0.5,
                              stratify = iris.iloc[:,4] # qual coluna é para estratificar 
                              )

# fazendo a mesma coisa para o conjunto de dados "infert", que possui estratos de
# tamanhos diferentes - amostra estratificada de 100 elementos


infert = pd.read_csv('infert.csv')
infert["education"].value_counts()

x1,_,y1,_ = train_test_split(infert.iloc[:,2:9],
                             infert.iloc[:,1],
                             test_size = 0.6, # ??? 
                             stratify = infert.iloc[:,1])

y1.value_counts()

100/248
"""
    ??? -> 
            original   amostra de 100 elementos
    6-11yrs    120        120/248*100 = 48
    12+ yrs    116        116/248*100 = 47
    0-5yrs      12         12/248*100 =  5 
    TOTAL      248                     100
"""
#Fez setindo assim:

_,x1,_,y1 = train_test_split(infert.iloc[:,2:9],
                             infert.iloc[:,1],
                             test_size = 100/248, # ??? 
                             stratify = infert.iloc[:,1])
