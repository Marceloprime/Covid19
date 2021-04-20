import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#data = requests.get('https://www.seade.gov.br/wp-content/uploads/2021/04/Dados-covid-19-estado.csv', allow_redirects=True)
#open('sao_paulo.csv', 'wb').write(data.content)

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


plt.plot(Cases[-30:-1], Date[-30:-1])
plt.show()