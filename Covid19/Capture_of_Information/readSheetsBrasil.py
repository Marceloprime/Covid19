# -*- coding: utf-8 -*-
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyexcel as pe
import matplotlib.pyplot as plt

totalCases = []
states = []
statesNames = ['Global','Brasil','Sao Paulo', 'Minas Gerais', 'Bahia', 'Santa Catarina', 'Rio Grande do Sul', 'Rio de Janeiro', 'Parana', 'Ceara', 'Goias', 'Para', 'Distrito Federal', 'Espirito Santo', 'Pernambuco', 'Maranhao', 'Amazonas', 'Mato Grosso', 'Paraiba', 'Piaui', 'Mato Grosso do Sul', 'Rio Grande do Norte', 'Sergipe', 'Alagoas', 'Rondonia', 'Tocantins', 'Roraima']
statesS = ['Global','BR','SP', 'MG', 'BA', 'SC', 'RS', 'RJ', 'PN', 'CE', 'GO', 'PA', 'DF', 'ES', 'PE', 'MA', 'AM', 'MT', 'PB', 'PI', 'MS', 'RN', 'SE', 'AL', 'RO', 'TO', 'RR']

sheet = np.array(pe.get_book(file_name="Brasil.ods"))

for i in range(1,28):
    totalCases.append(int(sheet[0][i][1]))

for i in range(1,28):
    aux = sheet[0][i][0].encode("utf-8")
    aux = aux.replace("\xc3\xa3","a")
    aux = aux.replace("\xc3\xa1","a")
    aux = aux.replace("\xc3\xad","i")
    aux = aux.replace("\xc3\xb4","o")
    aux = aux.replace("\xc3\xb4","o")
    flag = -1
    for n in statesNames:
        flag = flag + 1
        if n == aux:
            states.append(statesS[flag])
            break



for i in range(2, 27):
    plt.bar(states[i],totalCases[i])

plt.show()