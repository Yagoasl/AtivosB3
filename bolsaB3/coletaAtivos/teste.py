''' Acessa o site mas não coleta, a ideia era baixar um arquivo xlsx.
No entanto seria necessario pagar para acessar o download do arquivo.
Python, Selenium'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chromedriver_path = "D:\webdrivers\chromedriver.exe"
url = "https://br.tradingview.com/chart/"

driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.get(url)
sleep(5) 
driver.find_element(By.XPATH, "//div[7]/div/div/div[2]/button").click()
sleep(5)
driver.find_element(By.XPATH, "/html/body/div[2]/div[7]/div[2]/div[4]/div[3]/table/thead/tr/th[1]/div/div").click()

#row = driver.find_element(By.XPATH, "/html/body/div[2]/div[7]/div[2]/div[4]/div[4]/table/tbody/tr[1]").text
#print(row)


# 'div.tv-screener-toolbar__button tv-screener-toolbar__button--options tv-screener-toolbar__button--filters apply-common-tooltip common-tooltip-fixed').click
#driver.find_element(By.CLASS_NAME, "tv-control-checkbox__ripple js-ripple").click
#driver.find_element(By.CLASS_NAME, "tv-dialog__close js-dialog__close tv-tabbed-dialog__close").click
#driver.find_element(By.CLASS_NAME, "tv-data-table-sticky-wrapper tv-screener-sticky-header-wrapper").click
#driver.find_element(By.CLASS_NAME, "tv-data-table-sticky-wrapper tv-screener-sticky-header-wrapper").click

#rows = 1+len(driver.find_element(By.XPATH, "//body/div[2]/div[7]/div[2]/div[4]/div[4]/table/tbody/tr"))

#print(rows)

