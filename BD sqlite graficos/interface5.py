from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

# cuadroTexto=Entry(raiz)
cuadroTexto=Entry(miFrame)
# cuadroTexto.pack()
cuadroTexto.place(x=100, y=100)

nombreLabel=Label(miFrame, text="Nombre: ")   # Etiqueta en frente cuadroTexto Entry
nombreLabel.place(x=100,y=100)  # Al lado de cuadroTexto

raiz.mainloop()