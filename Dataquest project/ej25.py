#%% Calcular factorial de un numero
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"El factorial de {n} es {factorial}")
# %% Nueva celda encontrar numero primos de un numero e imprimir resultado
input_num = int(input("Ingrese un número para verificar si es primo: "))
def es_primo(num):      
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# %% Imprimir el resultado de la celda anterior
if es_primo(input_num): 
    print(f"{input_num} es un número primo.")
else:
    print(f"{input_num} no es un número primo.")    

# %% Nueva celda para calcular la suma de los primeros n números
n = 10
suma = sum(range(1, n + 1))
print(f"La suma de los primeros {n} números es {suma}")

# %%
