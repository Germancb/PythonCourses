hrs = input("Enter Hours:")
try :
    hrs = float(hrs)
except :
    print('Enter a numeric value')
    quit()
# hrs = float(hrs)
#
rate = input("Enter Rate:")
try :
    rate = float(rate)
except :
    print('Enter a numeric value')
    quit()
# rate = float(rate)
pay = hrs * rate
print("Pay:",pay)
    