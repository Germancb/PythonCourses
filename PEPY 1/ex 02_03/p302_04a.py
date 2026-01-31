from xml.sax.handler import DTDHandler

# This is the first line provide to you
k = 0
# hrs = input("Enter Hours:")
while k == 0:
    hrs = input("Enter Hours o fin :")
    if hrs =="fin":
        break
    try:
        hrs = float(hrs)
    except:
        print("Horas debe ser un número")
        continue
    k = 1
# rate = input("Enter Rate:")
    while k == 1:
        rate = input("Enter Rate o fin: ")
        if rate =="fin":
            break
        try:
            rate = float(rate)
        except:
            print("rate debe ser numerica")
            continue
        k = 2

if hrs == "fin" or rate =="fin":
    print("fin programa")
else:
    pay = hrs * rate
    print("Pay:", pay)