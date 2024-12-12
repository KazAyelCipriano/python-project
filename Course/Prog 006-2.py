#import login

import socket
import pandas as pd

#tabela = pd.read_csv(r"D:\\Pedro\Caixas.csv", sep=";")
#print(tabela)

import time
from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')
driver.get('http://www.google.com/');
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")
