from tkinter import *
import tkinter as tk
import requests
import json

def pegar_cotacao():
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacao = cotacao.json()
    cotacao_dollar = cotacao['USDBRL']['bid']
    cotacao_euro = cotacao['EURBRL']['bid']
    cotacao_bitcoin = cotacao['BTCBRL']['bid']
    
    texto = f'''
    Dollar:{cotacao_dollar}
    Euro:{cotacao_euro}
    Bitcoin:{cotacao_bitcoin}'''

    texto_cotacao['text'] = texto

janela = tk.Tk()
janela.title('Conversor de Moeda')
janela.geometry('400x200')

#botao
btn_converter = tk.Button(janela,text='COTAÇÃO MOEDAS',bg='green',command= pegar_cotacao)
btn_converter.grid(row=2,column=1, padx=5, pady=10)

#Label
texto= tk.Label(janela,text='Clique no botão abaixo para saber a cotação do Dollar/Euro/Bitcoin')
texto.grid(row=1, column=1,padx=5, pady=10)

texto_cotacao= tk.Label(janela,text='')
texto_cotacao.grid(row=3, column=1,padx=5, pady=10)


janela.mainloop()