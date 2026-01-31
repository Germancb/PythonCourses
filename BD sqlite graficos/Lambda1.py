"""def area_triangulo(base, altura):
    return (base*altura)/2
datos= miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0", END)

triangulo1=area_triangulo(2,3)
triangulo2=area_triangulo(6,12)

print(triangulo1)
print(triangulo2)"""

area_triangulo=lambda base, altura: (base*altura)/2

print(area_triangulo(6,8))
print(area_triangulo(45,12))

triangulo1=area_triangulo(2,3)
print(triangulo1)
