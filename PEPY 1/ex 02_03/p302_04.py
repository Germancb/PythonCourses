from xml.sax.handler import DTDHandler


10# This is the first line provide to ypu
hrs = input("Enter Hours:")
try:
    hrs = float(hrs)
except:
    print("Horas debe ser un número")
    exit()
# hrs = float(hrs)
rate = input("Enter Rate:")
try:
    rate = float(rate)
except:
    print("rate debe ser numerica)")
    exit()
pay = hrs * rate
print("Pay:", pay)
#