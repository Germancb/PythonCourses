from tkinter import *   # libreria tkinder

raiz=Tk()

raiz.title("Ventana de Pruebas")

# raiz.resizable(0,0)  # No se puede redimensionar la ventana Fañse False width heigh

# raiz.iconbitmap("gato.icon")  para que aparezca el gato si esta en folder graficos ext .ico
raiz.geometry("750x450")
raiz.config(bg="blue")

miFrame=Frame()    # otro cuedro Frame
# miFrame.pack(side="bottom")
miFrame.pack(side="left", anchor="n")   # arriba y a la izquierda
miFrame.config(bg="red")
miFrame.config(width="650", height="350")
raiz.mainloop()