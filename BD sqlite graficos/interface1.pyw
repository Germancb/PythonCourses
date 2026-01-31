from tkinter import *   # libreria tkinder

raiz=Tk()

raiz.title("Ventana de Pruebas")

raiz.resizable(0,0)  # No se puede redimensionar la ventana Fañse False width heigh

# raiz.iconbitmap("gato.icon")  para que aparezca el gato si esta en folder graficos ext .ico
raiz.geometry("650x350")
raiz.config(bg="blue")
raiz.mainloop()