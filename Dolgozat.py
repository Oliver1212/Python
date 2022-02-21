import random

f=open("adatok.txt","w")
f.write("1,2,3,4,5")

szam=input("Kérek egy számot: ")
print(szam)
print(random.random())

f.close()

f=open("adatok.txt","r")
print(f.read())
