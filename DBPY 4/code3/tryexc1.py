try:
    monto = float(input("Entre monto o valor del creditO: "))
    numpag = int(input("Entre un numero entero de pagos. Numero de meses entre 1 y 123:"))
    if numpag  < 0 or monto < 0:
        raise Exception("Ingresa un número de pagos y/o monto positivo ")
    if numpag > 12:
        raise Exception("Ingresa un número de pagos menor a 12 ")
except ValueError:
    print("Ingresa valor numérico: ")
except ZeroDivisionError:
    print("No puede incluir 0 pagos: ")
except Exception as un_error:
    print(un_error.args[0])
else:
    print("Solicitus exitosa: ")
    pago_mes = monto/numpag
    print("El pago mensuakl será de: ", pago_mes)


