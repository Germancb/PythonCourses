from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()

# miImagen=PhotoImage(file="mouse.gif")  =reemplazar mouse.gif ->ruta de la imagen
miImagen=PhotoImage(file="happynyear2023.png")   

miLabel=Label(miFrame, image=miImagen).place(x=100, y=200)
# miLabel.place(x=100, y=200)  #sitio del texto  distancias en pixeles
# Label(miFrame,text="Hola alumnos de Python").place(x=200,y=400) 
root.mainloop()