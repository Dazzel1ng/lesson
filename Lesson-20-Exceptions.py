import sys

filename = "Random"
while True:
 try:
    print("Inside TRY")
    myfiel = open(filename,mode='r', encoding="Latin-1")
 except Exception:
    print("Inside EXCEPT")
    print("Error Found!")
    filename =input("ENter Correct file name! : ")
 else:
    print("Indise ELSE")
    print(myfiel.read())
 finally:
    print("Inside FINALLY")

print("========================EOF======================")