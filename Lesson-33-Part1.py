from urllib import request

myUr1 = "http://www.astrahov.net"

otvet = request.urlopen(myUr1)
mytext1 = otvet.redlines()
mytext2 = otvet.read()
print(otvet)
print(mytext2)

for line in mytext1:
    print(line)
