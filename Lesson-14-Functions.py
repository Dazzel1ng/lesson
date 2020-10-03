def napeshatat_privetstvie(name):
    """Print Privetstvie"""
    print("Congratulations" + name + "wish you all the best!")


def summa(x, y):
    s = x + y
    return s

def factorial(x):
    """Claculate Factorial of number X"""
print("-------------------------------")
napeshatat_privetstvie("Nikita")
napeshatat_privetstvie("Vasya")

x= summa(33, 22)
print(x)


for i in range(1,10):
    print(str(i) + "!\t = " + factorial(i))


print(factorial(1))
print(factorial(5))
