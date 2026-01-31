# segunada funcion
def myfun02(manpar1,manpar2,outpar=True):
    if outpar:
        abc=manpar1
        efg=manpar2
    else:
        abc="xyz"
        efg="vwz"
    str1 = abc+" "+efg
    return str1

print(myfun02("german","cordoba"))
print(myfun02("luis","cordoba", False))
