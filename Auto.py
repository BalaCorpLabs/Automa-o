import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

arquivo_excel_1 = '1e2.xlsx'
arquivo_excel_2 = '3.xlsx'

df_dia_1 = pd.read_excel(arquivo_excel_1,sheet_name='dia1')
df_dia_2 = pd.read_excel(arquivo_excel_1,sheet_name='dia2')
df_dia_3 = pd.read_excel(arquivo_excel_2)

df_all = pd.concat([df_dia_1,df_dia_2,df_dia_3])

df_all.to_excel('consolidado.xlsx')

#print (df_all)

soma = df_all.groupby(['Nome']).sum()

#print(soma)

relatorio_bonito = soma.loc[:,"Nome":"Nota"]

print(relatorio_bonito)

relatorio_bonito.plot(kind='barh')

plt.show()