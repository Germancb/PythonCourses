import re  # re2.py
cadena="Vamos a aprender expresiones regulares"
textoBuscar="aprender"

textoEncontrado=re.search(textoBuscar, cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())