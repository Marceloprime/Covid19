import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


data = requests.get('https://www.seade.gov.br/wp-content/uploads/2021/04/Dados-covid-19-estado.csv', allow_redirects=True)
open('sao_paulo.csv', 'wb').write(data.content)

dataframe = pd.read_csv('sao_paulo.csv',encoding="latin-1", delimiter=";", usecols=["Data","Total de casos","Casos por dia","Óbitos por dia"])
datas = np.array(dataframe)

Date = []
Cases = []
CasesPerDay = []
Death = []

for x in datas:
    Date.append(x[0])
    Cases.append(int(x[1]))
    CasesPerDay.append(x[2])
    Death.append(x[3])


fig, ax = plt.subplots()
vector = np.array(range(0, 426))
ax.plot( vector, Cases,lw=2, marker='o', linestyle='dotted')
ax.set( xlabel='Casos', ylabel='Dias',title='Covid-19 in São Paulo')
plt.show()
os.remove("sao_paulo.csv")