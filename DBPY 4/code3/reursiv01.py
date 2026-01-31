# recursividad  rec01
def fact1(n):
    if n == 1 or n==0:
        return 1
    result= 1
    for i in range(2, n+1):
        result = result * i
    return result

print(fact1(5))