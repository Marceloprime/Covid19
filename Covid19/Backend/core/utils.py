import requests
import pandas as pd
import matplotlib.pyplot as plt


data = requests.get('https://www.seade.gov.br/wp-content/uploads/2021/04/Dados-covid-19-estado.csv', allow_redirects=True)
open('sao_paulo.csv', 'wb').write(data.content)

dataframe = pd.read_csv('sao_paulo.csv',encoding="latin-1", delimiter=";")
print(dataframe.columns[0][0])
#plt.plot(dataframe)