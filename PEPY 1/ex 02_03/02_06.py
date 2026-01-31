largest = None
smallest = None
while True:
    num = input("Enter a number or done after the last numeber")
    if num == "done":
        break
    try :
        num = float(num)
    #    print('Float:', num)
    except : 
        print("Invalid input")
        continue   
    print('Float:',num) 
    if smallest is None :
    	smallest = num              
    elif num < smallest : 
    	smallest = num
    #
    if largest is None :
        largest = num
    elif num > largest :
        largest = num
print("Maximum is", largest)
print("Minimum is", smallest) 