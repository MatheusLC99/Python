# criando um "robo" para dispara mensagem automaticamento no whatsapp com mensagem e numeros salvos no excel
import pandas as pd


contatos_df = pd.read_excel("Enviar.xlsx")
print(contatos_df)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

# login feito no whatsapp
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i,"Nome"]
    numero = contatos_df.loc[i,"Numero"]
    texto = urllib.parse.quote(f"Teste para {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(5)
