'''Pandas, python, coleta nome das empresas de um arquivo e puxa a variação pelas datas impostas'''
import pandas as pd
import pandas_datareader.data as web
import datetime as data

# Data de inicio da coleta
data_inicial = "01/01/2020"
# Data de fim da coleta
data_final = "01/01/2021"
# Código da empresa na B3 
empresa = 'PETR4.SA'

df = web.DataReader(empresa, data_source='yahoo', start=f'20-01-2022', end='21-07-2022')
print(df)
df.to_excel("historico.xlsx")

'''
empresas_df = pd.read_excel("historico.xlsx")

for empresa in empresas_df['Código']: 
    print(f"{empresa}:")
    df = web.DataReader(f'{empresa}', data_source='yahoo', start=data_inicial, end=data_final)
    print(df)
'''