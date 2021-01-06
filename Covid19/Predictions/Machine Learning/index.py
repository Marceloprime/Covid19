try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import pandas as pd

#Visualisation libraries
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import folium
from folium import plugins
import openpyxl # engine para abrir o arquivo xlsx
plt.rcParams['figure.figsize'] = 20,12

#Disable warnings
import warnings
warnings.filterwarnings('ignore')

#Learn how to read a .xls file by creating a dataframe using pandas
df = pd.read_excel('../../assets/Covid cases in India.xlsx', engine='openpyxl')
df_India = df.copy()

#Coordinates of India States and Union Territories
India_coord = pd.read_excel('../../assets/Indian Coordinates.xlsx', engine='openpyxl')


#Day by day data of India, Kora, Italy and Wunhan
dbd_India = pd.read_excel('../../assets/per_day_cases.xlsx',parse_dates=True, sheet_name='India', engine='openpyxl')
dbd_Italy = pd.read_excel('../../assets/per_day_cases.xlsx',parse_dates=True, sheet_name='Italy', engine='openpyxl')
dbd_Korea = pd.read_excel('../../assets/per_day_cases.xlsx',parse_dates=True, sheet_name='Korea', engine='openpyxl')
dbd_Wuhan = pd.read_excel('../../assets/per_day_cases.xlsx',parse_dates=True, sheet_name='Wuhan', engine='openpyxl')

df.drop(['Total Confirmed cases (Indian National)'], axis=1,inplace=True)
df['Total cases'] = df['Total Confirmed cases (Indian National)'] + df['Total COnfirmed cases (Foreifn National)]']
total_cases = df['Total cases'].sum()
print('Total number of confirmed COVID 2019 cases across India till date (22nd March, 2020): ', total_cases)

#Highlight dataframe
df.style.background_gradient(cmap='Reds')