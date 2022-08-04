''' Coleta parcial de cotação de ativos, salva em um arquivo xlsx.
Python, pandas, beautifulsoup, openpyxl'''

from django.test import TestCase
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.workbook import Workbook
from datetime import datetime, date
import time

html = urlopen("https://br.tradingview.com/markets/stocks-brazil/market-movers-all-stocks/")

bs = BeautifulSoup(html, 'html5lib')
linhas = bs.find_all('tr', {'class':'row-arjDAkRm listRow'})

codigo, preco, variacao_porcento_diaria, variacao_diaria, tendencia, volume, volume_preco, valor, pl, eps, empregados, setor = [], [], [], [], [], [], [], [], [], [], [], []

for i in linhas:
    children = i.findChildren("td")
    codigo.append(children[0].text)
    preco.append(children[1].text)
    variacao_porcento_diaria.append(children[2].text)
    variacao_diaria.append(children[3].text)
    tendencia.append(children[4].text)
    volume.append(children[5].text)
    volume_preco.append(children[6].text)
    valor.append(children[7].text)
    pl.append(children[8].text)     #relação preço/lucro
    eps.append(children[9].text)     #eps basico 12 meses
    empregados.append(children[10].text)
    setor.append(children[11].text)



df = pd.DataFrame({'Código': codigo, 'Preço': preco, 'Variação Diaria': variacao_diaria, 'Variação %, 1D': variacao_porcento_diaria, 'Tendência de Mercado': tendencia, 'Volume, 1D': volume, 'Volume*Preço, 1D': volume_preco, 'Valor de Mercado': valor, 'Relação Preço/lucro': pl, 'EPS (12M)': eps, 'Empregados': empregados, 'Setor': setor})
df.head()
df.to_excel('acoes.xlsx')
#df.write(Ativos)
#ibov= df.sort_values('Código',ascending=False)
#print(ibov)
#writer = pd.ExcelWriter('Acoes.xlsx')
#df.to_excel(writer)
#writer.save()
