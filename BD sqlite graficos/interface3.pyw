from tkinter import *   # libreria tkinder

raiz=Tk()

raiz.title("Ventana de Pruebas")

# raiz.iconbitmap("gato.icon")  para que aparezca el gato si esta en folder graficos ext .ico
raiz.geometry("750x450")
raiz.config(bg="blue")

miFrame=Frame()   #Frame mas sofosticado en bordes 
# miFrame.pack(side="bottom")
miFrame.pack(side="left", anchor="n")   # arriba y a la izquierda
miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
miFrame.config(relief="groove")
miFrame.config(cursor="hand2")

raiz.mainloop()