hrs = input("Enter Hours:")
while True:
    try :
        hrs = float(hrs)
    except :
        print('Error: Enter a numeric input')
        quit()
    rate = input("Enter Rate:")
    try :
    rate = float(rate)
except :
    print('Error: Enter a numeric input')
    quit()
pay = hrs * rate
print("Pay:",pay)
    