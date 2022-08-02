import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import pandas as pd

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#codigo, preco, variacao_porcento_diaria, variacao_diaria, tendencia, volume, volume_preco, valor, pl, eps, empregados, setor = [], [], [], [], [], [], [], [], [], [], [], []

chromedriver_path = "D:\webdrivers\chromedriver.exe"
url = "https://br.tradingview.com/markets/stocks-brazil/market-movers-all-stocks/"

driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.get(url)
sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div/div[2]/div[2]/div/button").click()
sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div/div[2]/div[2]/div/button").click()

acao = driver.find_element(By.CSS_SELECTOR,"row-arjDAkRm listRow")
print(acao)
#tables = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table")))

'''
for table in tables:
    for row in linha.find_elements(By.XPATH, ".//tr"):
        codigo.append(row.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/table/thead/tr/th[1]").__getattribute__('TextContent'))
        preco.append(row.find_element(By.XPATH,"./th[2]").__getattribute__('TextContent'))
        variacao_porcento_diaria.append(row.find_element(By.XPATH,"./th[3]").__getattribute__('TextContent'))
        variacao_diaria.append(row.find_element(By.XPATH,"./th[4]").__getattribute__('TextContent'))
        tendencia.append(row.find_element(By.XPATH,"./th[5]").__getattribute__('TextContent'))
        volume.append(row.find_element(By.XPATH,"./th[6]").__getattribute__('TextContent'))
        volume_preco.append(row.find_element(By.XPATH,"./th[7]").__getattribute__('TextContent'))
        valor.append(row.find_element(By.XPATH,"./th[8]").__getattribute__('TextContent'))
        pl.append(row.find_element(By.XPATH,"./th[9]").__getattribute__('TextContent'))     #relação preço/lucro
        eps.append(row.find_element(By.XPATH,"./th[10]").__getattribute__('TextContent'))     #eps basico 12 meses
        empregados.append(row.find_element(By.XPATH,"./th[11]").__getattribute__('TextContent'))
        setor.append(row.find_element(By.XPATH,"./th[12]").__getattribute__('TextContent'))

df = pd.DataFrame({'Código': codigo, 'Preço': preco, 'Variação Diaria': variacao_diaria, 'Variação %, 1D': variacao_porcento_diaria, 'Tendência de Mercado': tendencia, 'Volume, 1D': volume, 'Volume*Preço, 1D': volume_preco, 'Valor de Mercado': valor, 'Relação Preço/lucro': pl, 'EPS (12M)': eps, 'Empregados': empregados, 'Setor': setor})
print(df)
'''

'''for i in linhas:
    children = id.findChildren("td")
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
df.to_excel('acoes_att20.xlsx')'''