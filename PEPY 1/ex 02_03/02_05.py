score = input("Enter Score: ")
try :
    sc = float(score)
except :
    print("Error, please enter numeric input")
    quit()
if sc <= 0.0 :
    print("Error, Score no puede ser inferior a 0.0")
    quit()
elif sc > 1.0 :
    print("Error, Score no puede ser superior a 1.0")
    quit()
if sc >= 0.9 :
	print("A")
elif sc >= 0.8 :
	print("B")
elif sc >= 0.7 :
	print("C")
elif sc >= 0.6 :
	print("D")
else :
	print("F")