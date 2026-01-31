message1 = "Global Variable"
def myFunction():
 print( "\nINSIDE THE FUNCTION ")
#Global variables are accessible inside a function
print (message1)
#Declaring a local variable
message2 = "Local Variable "
print (message2)
'''
Calling the function
Note that myFunction() has no parameters.
Hence, when we call this function,
we use a pair of empty parentheses.
'''
myFunction()
