mystring = "bla bla bla"

name = "mr Vasya Pupkin"

print(name.title())
print(name.upper())
print(name.lower())

print("Privet stroka nomer1\n Privet stroka №2 \n\n Privet stroka №3")
print("Message: \n\tMessage \n\tMessage2 \n\tMessage3 \nEND")
print("Lower name:" + name.lower())
print("--------------------\n\n")
a = ".....dadya vasya......"
print(a)
print(a.rstrip())
print(a.lstrip())
print(a.strip())

a = ".....dadya vasya......"
a = a.strip(".")   #Udalenie to4ek
a = a.strip()      #Udalenie probelov
print(a)