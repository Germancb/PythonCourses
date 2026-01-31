import re  # re3.py
cadena="Vamos a aprender expresiones regulares. en python. python es un lenguaje de sintaxos sencilla"
textoBuscar="python"

# print(re.findall(textoBuscar, cadena))
texten=re.findall(textoBuscar, cadena)
print(texten," ", len(texten))
