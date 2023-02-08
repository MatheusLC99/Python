from tkinter import *
import tkinter
from datetime import datetime
import pyglet
pyglet.font.add_file("digital-7.ttf")

###### cores ######
cor1 = "#3d3d3d" # preto
cor2 = "#fafcff" # branco
cor3 = "#21c25c" # verde
cor4 = "#eb463b" # vermelho
cor5 = "#dedcdc" # cinza
cor6 = "#3080f0" # azul

fundo = cor1
letra = cor3

janela= Tk()
janela.title("Relógio Digital")
janela.geometry("360x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)


def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana=tempo.strftime("%A")
    dia=tempo.day
    mes=tempo.strftime("%b")
    ano=tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + " "+ str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(janela, text="", font=("digital-7 100"), bg=fundo, fg=letra)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela,text="",font=("digital-7 20"),bg=fundo, fg=letra)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()