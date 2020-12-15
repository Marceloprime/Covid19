from pyexcel_ods import get_data
import json
import numpy as np
import matplotlib.pyplot as plt

coutries = []
cases = [] 
#Deaths = json.dumps(get_data("Global.ods",start_column=3, column_limit=3,row_limit=238)) 
#Recov = json.dumps(get_data("Global.ods",start_column=4, column_limit=4,row_limit=238)) 


aux = json.dumps(get_data("Global.ods",start_column=1, column_limit=1,row_limit=238)) 
string = ''
for i in aux:
    if i == '[':
        continue
    if i == ']':
        continue
    if i == '"':
        if string == "{" or string == "Sheet1" or string == ": , " or string == ", ":
            string = ''
            continue
        coutries.append(string)
        string = ''
        continue
    string = string + i


aux2 = json.dumps(get_data("Global.ods",start_column=2, column_limit=1, row_limit=238)) 
string = ''
for i in aux2:
    if i == ",":
        continue
    if i == "[":
        if string =="{Sheet1:":
            string = ''
            continue
        if string == "":
            string = ''
            continue
        if string == "Cases":
            string = ''
            continue
        if string == "b":
            string = ''
            continue
        if string == "[":
            string = ''
            continue
        cases.append(int(float(string)))
        string = ''
        continue
    if i == ']':
        continue
    if i == '"':
        continue
    if i == ' ':
        continue
    string = string + i

cases = np.array(cases)

for i in range(10):
    plt.bar(coutries[i],cases[i])
plt.ylim(0, cases[0])
plt.show()



 
