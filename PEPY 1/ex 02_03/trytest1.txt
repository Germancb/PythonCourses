try:
	useri = int(input("entre nuemro entero 1"))
	useri2 = int(input("Entre numero 2"))
	result = useri/useri2
	print ("The answer is ", result)
	myFile = open("missing.txt", 'r')
except ValueError:
	print ("Error: You did not enter a number")
except ZeroDivisionError:
	print ("Error: Cannot divide by zero")
except Exception as e:
	print ("Unknown error")


