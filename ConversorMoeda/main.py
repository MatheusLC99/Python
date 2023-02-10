from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image, ImageOps, ImageDraw, ImageTk
import requests
import json
import string

janela = tk.Tk()
janela.title('Conversor Monetário')
janela.geometry('300x320')
janela.resizable(width=FALSE, height=FALSE)

moeda = ['BRL','EUR','USD']

def CalculaValorMoeda():
    
    moeda_de = combo_de.get()
    moeda_para = combo_para.get()
    valor_entrada = valor.get()
    #---------> Consultando Valores -----------
    resposta = requests.get('https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_para))
    dados = json.loads(resposta.text)
    resp_api = (dados['rates'][moeda_de])

    if moeda_para == 'USD':
        simbolo = '$'
    elif moeda_para == 'EUR':
        simbolo = '£'
    else:
        simbolo='R$'

    cambio = float(resp_api) * float(valor_entrada)
    moeda_eq = simbolo + '{:,.2f}'.format(cambio)

    resultado['text'] = moeda_eq
#---------> Cabecalho ----------
cabecalho = Frame(janela, width=300, height=60, padx=0, pady=0,bg='blue',relief='flat')
cabecalho.grid(row=0,column=0, columnspan=2)

icon = Image.open(os.path.join(r'C:\Estudos\Python\ConversorMoeda\icone.png'))
icon = icon.resize((40,40), Image.LANCZOS)
icon = ImageTk.PhotoImage(icon)

titulo = Label(cabecalho, image=icon, compound=LEFT, text='Conversor Moeda',pady=30,padx=15,anchor=CENTER,bg='blue',relief='flat', font='Arial 16 bold', fg='lightyellow')
titulo.place(x=10,y=-20)

#----------> centro ----------
corpo = Frame(janela, width=300, height=260, padx=0, pady=5,bg='green',relief='flat')
corpo.grid(row=1,column=0, sticky=NSEW)

resultado = Label(corpo, text='',width= 14, height=2,anchor=CENTER, bg='white',relief='solid', font='Arial 14 bold', fg='black')
resultado.place(x=65,y=10)

label_De = Label(corpo, text='De:',width= 8, height=2,anchor=NW, bg='green',relief='flat', font='Arial 10', fg='black')
label_De.place(x=65,y=70)

label_Para = Label(corpo, text='Para:',width= 8, height=2,anchor=NW, bg='green',relief='flat', font='Arial 10', fg='black')
label_Para.place(x=170,y=70)

combo_de = ttk.Combobox(corpo, width=5, height=1,justify=CENTER, font=('Arial 12'))
combo_de.place(x=65, y=90)
combo_de['values'] = (moeda)

combo_para = ttk.Combobox(corpo, width=5, height=1,justify=CENTER, font=('Arial 12'))
combo_para.place(x=170, y=90)
combo_para['values'] = (moeda)

valor = tk.Entry(corpo,width=19, justify=CENTER, font='Arial 12', relief='solid')
valor.place(x=65, y=130)

#----------> Botão ---------
botao = tk.Button(corpo, text='CONVERTER', width=16, padx=5, height=1, font='Arial 12 bold', relief='raised', overrelief= RIDGE, bg='blue', fg='black', command=CalculaValorMoeda)
botao.place(x=65, y=170)

janela.mainloop()