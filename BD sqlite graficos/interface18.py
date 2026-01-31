from tkinter import *
from tkinter import filedialog
root=Tk()

def abreArchivo():
#   archivo=filedialog.askopenfile(title="Abrir", initialdir="C:")
    archivo=filedialog.askopenfile(title="Abrir", initialdir="C:",filetype=(("Archivos Excel","*.xlsx"),
                                                                            ("Archivos texto","*.txt"),("Todos los archivos","*.*")))
    print(archivo)

Button(root,text="Abrir archivo",command=abreArchivo).pack()




root.mainloop()