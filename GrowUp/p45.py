consnum= [1, 2, 3, 4, 5]
# Function to remove one number of the number list
def remove_num(num):
    consnum.remove(num)
    return consnum
print(remove_num(3))
# Function to add one number to the number list
def add_num(num):
    consnum.append(num)
    return consnum
print(add_num(6))
# Function to replace one number with another number in the number list
def replace_num(oldnum, newnum):        
    index = consnum.index(oldnum)
    consnum[index] = newnum
    return consnum
