def doblar(referencia, valor):
    referencia *=2
    valor *=2
    print("Durante: ", referencia, valor)
    return valor


estructura=["a", "b","c"]
primv="abc"
doblar(estructura, primv)
print("Despues: ",estructura, primv)

